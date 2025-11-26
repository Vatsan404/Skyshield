# Skyshield
🛡️ Skyshield — Cloud Breach Simulation & Defense Automation System (CBSDAS)

Skyshield is a cloud security project designed to simulate common cloud attacks and detect misconfigurations across AWS services.
It includes attack modules, detection modules, and a simple Flask-based dashboard to visualize security risks in real time.

This project is intended for learning, research, and demonstrating cloud security concepts.

🚀 Features

Attack Simulation

Stop CloudTrail logging

Public S3 bucket creation

IAM access key creation

EC2 port exposure

S3 data exfiltration

Security Group lockouts

Detection Engine

S3 public access detection

CloudTrail tampering detection

IAM anomalies detection

EC2 open ports detection

S3 exfiltration detection

Dashboard

Real-time results

API-based detection outputs

Simple and clean Flask UI

CLI Support

Execute all attacks using command-line arguments

📁 Project Structure
Skyshield/
├── attacks/                 # Cloud attack modules
├── detection/               # Detection engine modules
├── dashboard/               # Flask dashboard
├── cbsdas.py                # Main CLI tool
├── cli.py                   # CLI parser
├── requirements.txt         # Dependencies
└── README.md                # Documentation

⚙️ Installation
1. Clone the repository
git clone https://github.com/Vatsan404/Skyshield.git
cd Skyshield

2. Install dependencies
pip3 install -r requirements.txt

3. Configure AWS (EC2 Recommended)

Attach an IAM role to EC2 with these policies:

AmazonS3ReadOnlyAccess

AmazonEC2ReadOnlyAccess

CloudTrailReadOnlyAccess

IAMReadOnlyAccess

Ensure the EC2 region matches your AWS resources.

▶️ Usage
Start the Dashboard
cd dashboard
python3 app.py


Open in browser:

http://<your-ec2-public-ip>:8000

Run an Attack from CLI

Examples:

python3 cbsdas.py cloudtrail_stop --trail project-trial
python3 cbsdas.py s3_public --bucket example-bucket
python3 cbsdas.py ec2_open_ports

Run All Detections
python3 detection/run_all_detections.py

📌 Examples
Example CLI command:
python3 cbsdas.py s3_public --bucket test-bucket

Example API endpoint:
GET /api/detections


Returns JSON with all detector results.

👨‍💻 Contributors

Srivatsan V (Vatsan404)

Project Developer

Cloud & Cybersecurity Enthusiast

📚 Additional Notes

This project is intended only for learning.

Use responsibly inside your own AWS test environment.

Do not run against production or unknown AWS accounts.
