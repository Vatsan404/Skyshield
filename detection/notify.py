import boto3

sns = boto3.client("sns")

TOPIC_ARN = "arn:aws:sns:eu-north-1:637423476013:project-alerts"

def send_alert(message):
    """
    Unified SNS alert sender for CBSDAS detections.
    Accepts plain text, sends to SNS topic.
    """
    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=str(message),      # 🔥 ensure clean, readable output
        Subject="⚠️ CBSDAS Security Alert"
    )
