import boto3

def detect_public_bucket(bucket_name):
    s3 = boto3.client("s3")
    findings = []

    # 1) Check Public Access Block
    try:
        pab = s3.get_public_access_block(Bucket=bucket_name)
        cfg = pab.get("PublicAccessBlockConfiguration", {})
    except s3.exceptions.NoSuchPublicAccessBlockConfiguration:
        cfg = {}

    is_block_off = (
        not cfg.get("BlockPublicAcls", True)
        or not cfg.get("IgnorePublicAcls", True)
    )

    # 2) Check ACL permissions
    acl = s3.get_bucket_acl(Bucket=bucket_name)

    for grant in acl.get("Grants", []):
        grantee = grant.get("Grantee", {})
        permission = grant.get("Permission")

        if grantee.get("URI") == "http://acs.amazonaws.com/groups/global/AllUsers":
            findings.append({
                "bucket": bucket_name,
                "issue": "Bucket ACL allows public access",
                "permission": permission
            })

    # ❌ NO SNS HERE  
    # Only return data. app.py will check + send SNS.

    # Return findings only when public access is confirmed
    if is_block_off and findings:
        return findings

    return []
