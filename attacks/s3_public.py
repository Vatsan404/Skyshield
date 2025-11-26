import boto3

def simulate_s3_public(bucket_name):
    s3 = boto3.client('s3')

    print(f"[+] Making bucket public: {bucket_name}")

    s3.put_bucket_acl(
        Bucket=bucket_name,
        ACL='public-read'
    )

    print(f"[+] Bucket {bucket_name} is now PUBLIC")
