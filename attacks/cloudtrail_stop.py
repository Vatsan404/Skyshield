import boto3

def simulate_cloudtrail_stop(trail_name):
    cloudtrail = boto3.client('cloudtrail')

    print(f"[+] Attempting to STOP CloudTrail logging for: {trail_name}")

    cloudtrail.stop_logging(
        Name=trail_name
    )

    print(f"[!] CloudTrail logging STOPPED for trail: {trail_name}")
