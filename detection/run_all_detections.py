import json
from detection.s3_public_detector import detect_public_bucket
from detection.ec2_open_detector import detect_open_security_groups
from detection.cloudtrail_tamper_detector import detect_cloudtrail_tampering
from detection.iam_detector import detect_iam_anomalies
from detection.s3_exfiltration_detector import detect_s3_exfiltration

def run_all_checks():
    return {
        "s3_public": detect_public_bucket("cloud-project-acl-bucket"),
        "ec2_open_ports": detect_open_security_groups(),
        "cloudtrail_tampering": detect_cloudtrail_tampering(),
        "iam_anomalies": detect_iam_anomalies(),
        "s3_exfiltration": detect_s3_exfiltration("cloud-project-acl-bucket"),
    }

if __name__ == "__main__":
    print(json.dumps(run_all_checks(), indent=4))
