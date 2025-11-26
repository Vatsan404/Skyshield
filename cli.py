#!/usr/bin/env python3
import os
import subprocess
import sys
import pyfiglet

# ===== Colors =====
if sys.stdout.isatty():
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
else:
    BLUE = CYAN = GREEN = YELLOW = RED = RESET = ""


# ==========================
#     PRINT BIG BANNER
# ==========================
def print_banner():
    banner = pyfiglet.figlet_format("SKYSHIELD", font="big")
    print(f"{BLUE}{banner}{RESET}")
    print(f"{YELLOW}[-] Tool Created by VATSAN V{RESET}\n")
    print(f"{CYAN}[::] Select An Attack Simulation [::]{RESET}\n")


# ==========================
#  ATTACK DEFINITIONS
# ==========================
ATTACKS = {
    "1": {
        "name": "S3 Public Exposure",
        "attack_key": "s3_public",
        "params": [
            {"flag": "--bucket", "prompt": "Enter S3 bucket name"}
        ],
    },
    "2": {
        "name": "EC2 Open Security Group",
        "attack_key": "ec2_open",
        "params": [
            {"flag": "--sg", "prompt": "Enter Security Group ID"}
        ],
    },
    "3": {
        "name": "IAM Privilege Escalation (Attach Admin Policy)",
        "attack_key": "iam_escalation",
        "params": [
            {"flag": "--user", "prompt": "Enter IAM username"}
        ],
    },
    "4": {
        "name": "CloudTrail Stop Logging",
        "attack_key": "cloudtrail_stop",
        "params": [
            {"flag": "--trail", "prompt": "Enter CloudTrail Trail Name"}
        ],
    },
    "5": {
        "name": "IAM Access Key Creation",
        "attack_key": "iam_access_key",
        "params": [
            {"flag": "--user", "prompt": "Enter IAM username"}
        ],
    },
    "6": {
        "name": "CloudTrail Log Deletion (S3)",
        "attack_key": "cloudtrail_delete_logs",
        "params": [
            {"flag": "--bucket", "prompt": "Enter CloudTrail Log Bucket"},
            {"flag": "--prefix", "prompt": "Enter Log Prefix (AWSLogs) (press Enter to skip)"},
        ],
    },
    "7": {
        "name": "S3 External Exfiltration",
        "attack_key": "s3_exfil_external",
        "params": [
            {"flag": "--source", "prompt": "Enter Source Bucket"},
            {"flag": "--dest", "prompt": "Enter Attacker Bucket"},
            {"flag": "--prefix", "prompt": "Enter Prefix"},
        ],
    },
    "8": {
        "name": "EC2 Stop Instance",
        "attack_key": "ec2_stop",
        "params": [
            {"flag": "--instance", "prompt": "Enter Instance ID"},
        ],
    },
    "9": {
        "name": "IAM Backdoor User Creation",
        "attack_key": "iam_backdoor",
        "params": [
            {"flag": "--user", "prompt": "Enter Backdoor Username"},
        ],
    },
    "10": {
        "name": "Security Group Lockout (Remove SSH)",
        "attack_key": "sg_lockout",
        "params": [
            {"flag": "--sg", "prompt": "Enter Security Group ID"},
        ],
    },
}


# ==========================
#   UTIL FUNCTIONS
# ==========================
def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")


def print_menu():
    clear_screen()
    print_banner()

    for key in sorted(ATTACKS.keys(), key=lambda x: int(x)):
        print(f"[{key.zfill(2)}] {ATTACKS[key]['name']}")

    print("\n[99] Exit\n")


def build_command(selection: str):
    attack = ATTACKS[selection]
    cmd = ["python3", "cbsdas.py", attack["attack_key"]]

    print(f"\n{YELLOW}[>>] Selected: {attack['name']}{RESET}\n")

    for p in attack["params"]:
        raw = input(f"{CYAN}{p['prompt']}{RESET}: ").strip()

        # allow blank only for prefix
        if raw == "" and p["flag"] == "--prefix":
            continue

        while raw == "":
            print(f"{RED}[-] Value cannot be empty.{RESET}")
            raw = input(f"{CYAN}{p['prompt']}{RESET}: ").strip()

        cmd.append(p["flag"])
        cmd.append(raw)

    return cmd


# ==========================
#           MAIN
# ==========================
def main():
    while True:
        print_menu()
        choice = input(f"{YELLOW}[-] Select an option : {RESET}").strip()

        if choice in ("99", "0"):
            print(f"{GREEN}\n[+] Exiting SKYSHIELD CLI. Stay Safe!{RESET}\n")
            break

        if choice not in ATTACKS:
            print(f"{RED}[-] Invalid option.{RESET}")
            input(f"{CYAN}Press Enter to continue...{RESET}")
            continue

        cmd = build_command(choice)

        # Show exact command
        print("\n" + "-" * 60)
        print(f"{BLUE}Command to run:{RESET}")
        print("  " + " ".join(cmd))
        print("-" * 60)

        confirm = input(f"{YELLOW}Proceed? (y/n): {RESET}").strip().lower()
        if confirm != "y":
            print(f"{RED}[-] Canceled.{RESET}")
            input(f"{CYAN}Press Enter...{RESET}")
            continue

        print(f"{GREEN}\n[+] Running attack...\n{RESET}")

        # Run command safely without breaking CLI
        try:
            subprocess.run(cmd, check=False)
        except Exception as e:
            print(f"{RED}[-] Error occurred, but CLI will continue.{RESET}")
            print(f"{RED}{str(e)}{RESET}")

        input(f"{CYAN}Press Enter to return to menu...{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[-] Interrupted by user. Exiting SKYSHIELD...{RESET}\n")
        sys.exit(0)
