import boto3

def detect_iam_anomalies():
    iam = boto3.client("iam")
    findings = []

    # 1) Detect new IAM users (last 4 hours)
    users = iam.list_users()["Users"]
    for user in users:
        # User.CreateDate is datetime, convert to timestamp
        if (user["CreateDate"].timestamp()):
            findings.append({
                "user": user["UserName"],
                "issue": "New IAM user recently created"
            })

    # 2) Detect AdministratorAccess policy
    for user in users:
        policies = iam.list_attached_user_policies(UserName=user["UserName"])
        for policy in policies["AttachedPolicies"]:
            if policy["PolicyName"] == "AdministratorAccess":
                findings.append({
                    "user": user["UserName"],
                    "issue": "User has AdministratorAccess policy"
                })

    # 3) Detect access keys
    for user in users:
        keys = iam.list_access_keys(UserName=user["UserName"])["AccessKeyMetadata"]
        for key in keys:
            findings.append({
                "user": user["UserName"],
                "issue": "User has active access key",
                "access_key": key["AccessKeyId"]
            })

    return findings
