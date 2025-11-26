import boto3

def simulate_ec2_open_ports(security_group_id):
    ec2 = boto3.client('ec2')

    print(f"[+] Opening ALL ports on Security Group: {security_group_id}")

    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': '-1',   # all protocols
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            }
        ]
    )

    print(f"[+] Security Group {security_group_id} is now OPEN to the entire internet!")
