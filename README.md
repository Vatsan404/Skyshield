# 🛡️ **Skyshield – Cloud Breach Simulation & Defense Automation System (CBSDAS)**

**Skyshield** is a powerful cloud security project designed to simulate real-world cloud attacks and detect misconfigurations across AWS environments.  
It helps learners, cloud engineers, and cybersecurity analysts understand attacker behavior, cloud threats, and defensive monitoring through automated tools.

Skyshield includes AWS attack modules, detection engines, and a Flask-based dashboard to visualize risks in real time.

---

## 📚 **Table of Contents**
- [ℹ️ About](#about)
- [✨ Features](#features)
- [🧩 Requirements](#requirements)
- [⚙️ Installation](#installation)
- [🚀 Usage](#usage)
- [📝 Final Notes](#final-notes)
- [📄 License](#license)

---

## ℹ️ **About**

**Skyshield (CBSDAS)** is a complete cloud security simulation toolkit built in Python.  
It can perform cloud attack simulations such as:

- CloudTrail tampering  
- IAM backdoor creation  
- S3 data exposure  
- EC2 security group misconfiguration  
- S3 data exfiltration  

It also includes a detection engine that audits AWS environments for misconfigurations and threats.  
A web dashboard (Flask) displays security alerts, detection results, and overall cloud posture in real time.

This project is ideal for:

- Cloud security students  
- Red teamers  
- Blue team defenders  
- SOC and DFIR learners  
- Anyone building AWS security skills  

---

## ✨ **Features**

- ☁️ **Cloud Attack Simulation**
  - Stop or delete CloudTrail logs  
  - Create public S3 buckets  
  - Generate IAM Access Keys  
  - Expose EC2 ports (0.0.0.0/0)  
  - Trigger SG lockouts  
  - Exfiltrate S3 data  
  - Stop EC2 instances  

- 🔍 **Threat Detection Engine**
  - Detect CloudTrail tampering  
  - Find public S3 buckets  
  - Identify IAM anomalies  
  - Detect EC2 open ports  
  - Catch S3 exfiltration attempts  

- 🌐 **Web Dashboard (Flask)**
  - Real-time cloud security overview  
  - API-based detection updates  
  - Clean and simple UI  

- 🧰 **CLI-Based Execution**
  - Full attack automation  
  - Easy command-line interface  

---

## 🧩 **Requirements**

To run Skyshield, you need:

- Python **3.8+**
- AWS EC2 Instance (Recommended)
- IAM Role with:
  - AmazonS3ReadOnlyAccess  
  - AmazonEC2ReadOnlyAccess  
  - CloudTrailReadOnlyAccess  
  - IAMReadOnlyAccess  

Python dependencies (all included in `requirements.txt`):

- `boto3`
- `flask`
- `requests`
- `json`
- Any other libraries already inside your file

---

## ⚙️ **Installation**

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Vatsan404/Skyshield.git
cd Skyshield
pip3 install -r requirements.txt

## 🚀 **Usage**
▶️ Start the Dashboard
cd dashboard
python3 app.py


Access in browser:

http://<EC2_PUBLIC_IP>:8000

## ▶️ **Run Attack Modules (CLI)**
Examples:

python3 cbsdas.py cloudtrail_stop --trail project-trial

## **📝 Final Notes**

Skyshield is built to make cloud breach simulation and defense accessible to beginners and professionals.
It demonstrates both attack paths (red teaming) and security detection (blue teaming).

Feel free to explore, extend, or modify the project for learning or research.

Contributions, suggestions, and improvements are always welcome!
