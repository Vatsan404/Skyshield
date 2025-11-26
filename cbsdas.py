import argparse

# Import all attack functions
from attacks.s3_public import simulate_s3_public
from attacks.iam_escalation import simulate_iam_escalation
from attacks.ec2_open_ports import simulate_ec2_open_ports
from attacks.cloudtrail_stop import simulate_cloudtrail_stop
from attacks.iam_access_key import simulate_iam_access_key
from attacks.ec2_stop import simulate_ec2_stop
from attacks.iam_backdoor import simulate_iam_backdoor
from attacks.cloudtrail_delete_logs import simulate_cloudtrail_log_delete
from attacks.s3_exfiltrate_external import simulate_s3_exfiltrate
from attacks.sg_lockout import simulate_sg_lockout

def main():
    parser = argparse.ArgumentParser(description="CBSDAS Attack Simulator")
    parser.add_argument("attack", help="Attack to simulate")
    parser.add_argument("--bucket", help="S3 bucket name")
    parser.add_argument("--user", help="IAM username")
    parser.add_argument("--sg", help="Security Group ID")
    parser.add_argument("--trail", help="CloudTrail name")
    parser.add_argument("--source", help="Source S3 bucket")
    parser.add_argument("--dest", help="Destination S3 bucket")
    parser.add_argument("--prefix", help="Prefix filter", default="")
    parser.add_argument("--instance", help="EC2 Instance ID")

    args = parser.parse_args()

    # S3 Public Exposure
    if args.attack == "s3_public":
        if not args.bucket:
            print("[-] Usage: python3 cbsdas.py s3_public --bucket <bucket>")
            return
        simulate_s3_public(args.bucket)

    # IAM Privilege Escalation
    elif args.attack == "iam_escalation":
        if not args.user:
            print("[-] Usage: python3 cbsdas.py iam_escalation --user <username>")
            return
        simulate_iam_escalation(args.user)

    # EC2 Open Security Group
    elif args.attack == "ec2_open":
        if not args.sg:
            print("[-] Usage: python3 cbsdas.py ec2_open --sg <security-group-id>")
            return
        simulate_ec2_open_ports(args.sg)

    # CloudTrail Stop Logging
    elif args.attack == "cloudtrail_stop":
        if not args.trail:
            print("[-] Usage: python3 cbsdas.py cloudtrail_stop --trail <trail-name>")
            return
        simulate_cloudtrail_stop(args.trail)

    # IAM Access Key Creation
    elif args.attack == "iam_access_key":
        if not args.user:
            print("[-] Usage: python3 cbsdas.py iam_access_key --user <username>")
            return
        simulate_iam_access_key(args.user)
    # EC2 Stop Instance
    elif args.attack == "ec2_stop":
        simulate_ec2_stop(args.instance)
    # IAM Backdoor User Creation
    elif args.attack == "iam_backdoor":
        simulate_iam_backdoor(args.user)
    # CloudTrail Log Deletion
    elif args.attack == "cloudtrail_delete_logs":
        simulate_cloudtrail_log_delete(args.bucket, args.prefix)
    # S3 Exfiltration to External Bucket
    elif args.attack == "s3_exfil_external":
        simulate_s3_exfiltrate(args.source, args.dest, args.prefix)
    # Security Group Lockout
    elif args.attack == "sg_lockout":
        simulate_sg_lockout(args.sg)



    else:
        print(f"[-] Unknown attack: {args.attack}")


if __name__ == "__main__":
    main()
