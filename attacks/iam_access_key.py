import boto3

def simulate_iam_access_key(user_name):
    iam = boto3.client('iam')

    print(f"[+] Creating a new access key for user: {user_name}")

    response = iam.create_access_key(
        UserName=user_name
    )

    access_key = response['AccessKey']['AccessKeyId']
    secret_key = response['AccessKey']['SecretAccessKey']

    print(f"[+] Access key created for {user_name}")
    print(f"    AccessKeyId: {access_key}")
    print(f"    SecretAccessKey: {secret_key}")
    print("[!] Store these keys securely for testing (DO NOT use in real production).")

