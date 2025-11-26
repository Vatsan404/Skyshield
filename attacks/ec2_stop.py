import boto3

def simulate_ec2_stop(instance_id):
    ec2 = boto3.client("ec2")

    ec2.stop_instances(InstanceIds=[instance_id])

    print(f"[+] EC2 Instance STOP initiated: {instance_id}")
