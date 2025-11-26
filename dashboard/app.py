import sys
import os
import subprocess
import json
from flask import Flask, render_template, jsonify

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

app = Flask(__name__)

def run_detections():
    # Force subprocess to run inside the project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    result = subprocess.check_output(
        ["python3", "-m", "detection.run_all_detections"],
        text=True,
        cwd=project_root   # <<< IMPORTANT FIX
    )
    return json.loads(result)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/detections")
def api_detections():
    try:
        data = run_detections()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
from flask import Flask, jsonify
import boto3
import json
import time

# === IMPORT DETECTION MODULES ===
from detection.s3_public_detector import detect_public_bucket
from detection.ec2_open_detector import detect_open_security_groups
from detection.cloudtrail_tamper_detector import detect_cloudtrail_tampering
from detection.iam_detector import detect_iam_anomalies
from detection.s3_exfiltration_detector import detect_s3_exfiltration

sns = boto3.client("sns")
TOPIC_ARN = "arn:aws:sns:eu-north-1:637423476013:project-alerts"

app = Flask(__name__)

# Store previous results to detect NEW issues only
previous_findings = {
    "s3_public": [],
    "ec2_open_ports": [],
    "cloudtrail_tampering": [],
    "iam_anomalies": [],
    "s3_exfiltration": []
}


# === SNS ALERT FUNCTION ===
def send_alert(finding):
    try:
        sns.publish(
            TopicArn=TOPIC_ARN,
            Message=json.dumps(finding, indent=4),
            Subject="⚠️ CBSDAS SECURITY ALERT"
        )
        print("[+] SNS Alert Sent:", finding)
    except Exception as e:
        print("[ERROR] SNS Failed:", e)


# === RUN ALL DETECTIONS ===
def run_all_detections():
    return {
        "s3_public": detect_public_bucket("cloud-project-acl-bucket"),
        "ec2_open_ports": detect_open_security_groups(),
        "cloudtrail_tampering": detect_cloudtrail_tampering(),
        "iam_anomalies": detect_iam_anomalies(),
        "s3_exfiltration": detect_s3_exfiltration("cloud-project-acl-bucket"),
    }


# === API ROUTE FOR DASHBOARD ===
@app.route("/api/detections")
def api_detections():
    global previous_findings

    # run detections
    current = run_all_detections()

    # check for NEW issues
    for category in current:
        for item in current[category]:
            if item not in previous_findings[category]:   # NEW FINDING
                send_alert({
                    "type": category,
                    "details": item,
                    "time": time.strftime("%Y-%m-%d %H:%M:%S")
                })

    previous_findings = current  # update history

    return jsonify(current)


# === START FLASK ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
