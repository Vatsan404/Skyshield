import boto3
import json

def detect_s3_exfiltration(bucket_name):
    cloudtrail = boto3.client("cloudtrail")
    findings = []

    # Look for S3 CopyObject logs
    response = cloudtrail.lookup_events(
        LookupAttributes=[{
            "AttributeKey": "EventName",
            "AttributeValue": "CopyObject"
        }],
        MaxResults=50
    )

    for event in response.get("Events", []):
        # CloudTrailEvent is a STRING → parse JSON
        raw = json.loads(event["CloudTrailEvent"])

        req = raw.get("requestParameters", {})
        if not req:
            continue

        source_bucket = req.get("sourceBucketName")
        dest_bucket = req.get("destinationBucketName")

        # Ensure the event is about S3 object copy
        if not source_bucket or not dest_bucket:
            continue

        # Detect exfiltration from our bucket
        if source_bucket == bucket_name:
            findings.append({
                "bucket": bucket_name,
                "issue": "S3 EXFILTRATION DETECTED (CopyObject)",
                "source_bucket": source_bucket,
                "destination_bucket": dest_bucket,
                "event_time": event["EventTime"].strftime("%Y-%m-%d %H:%M:%S"),
                "user": event.get("Username", "Unknown")
            })

    # ❌ No SNS alert here  
    # Flask app will call send_alert() ONLY when findings exist

    return findings
