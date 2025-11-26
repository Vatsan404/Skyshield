import boto3

def detect_open_security_groups():
    ec2 = boto3.client("ec2")
    findings = []

    # Get all security groups
    response = ec2.describe_security_groups()

    for sg in response["SecurityGroups"]:
        sg_id = sg["GroupId"]
        sg_name = sg.get("GroupName", "")

        for rule in sg.get("IpPermissions", []):
            for ip_range in rule.get("IpRanges", []):
                if ip_range.get("CidrIp") == "0.0.0.0/0":
                    findings.append({
                        "security_group": sg_id,
                        "name": sg_name,
                        "protocol": rule.get("IpProtocol"),
                        "from_port": rule.get("FromPort"),
                        "to_port": rule.get("ToPort"),
                        "issue": "Security Group allows 0.0.0.0/0 (open to world)"
                    })

    return findings   # 👉 ONLY RETURN DATA (no SNS here)
