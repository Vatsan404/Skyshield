import boto3

def simulate_sg_lockout(sg_id):
    ec2 = boto3.client("ec2")

    print(f"[+] Removing SSH access from Security Group: {sg_id}")

    ec2.revoke_security_group_ingress(
        GroupId=sg_id,
        IpProtocol="tcp",
        FromPort=22,
        ToPort=22,
        CidrIp="0.0.0.0/0"
    )

    print(f"[!] SSH access REMOVED! You are locked out.")
