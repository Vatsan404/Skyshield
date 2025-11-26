import boto3

def detect_cloudtrail_tampering():
    ct = boto3.client("cloudtrail")

    findings = []

    # Get all trails
    trails = ct.describe_trails()['trailList']

    for trail in trails:
        name = trail['Name']
        status = ct.get_trail_status(Name=name)

        # If CloudTrail logging is OFF → alert
        if status.get("IsLogging") is False:
            findings.append({
                "trail": name,
                "issue": "CloudTrail logging is STOPPED"
            })

        # Check delivery errors (ex: attacker changed bucket permissions)
        error_msg = status.get("LatestDeliveryError")
        if error_msg:
            findings.append({
                "trail": name,
                "issue": f"Delivery error: {error_msg}"
            })

    return findings
