import getpass
import subprocess
import time
import os

# Load leaked credentials
leaked = {}
with open("leaked_credentials.txt") as f:
    for line in f:
        user, pwd = line.strip().split(":")
        leaked[user] = pwd

print("=== Simulated Colonial VPN Login ===")
username = input("Username: ")
password = getpass.getpass("Password: ")

MFA_ENABLED = False  # Change to True to simulate protection

# Auth logic
if username in leaked and leaked[username] == password:
    print("\n✅ [ACCESS GRANTED] VPN login successful.")
    if MFA_ENABLED:
        print("🔐 MFA enabled - attacker blocked.")
    else:
        print("❌ No MFA detected - attacker proceeds...")
        time.sleep(1)
        print("💣 Launching ransomware...\n")
        # Launch encryption script
        subprocess.run(["py", "Test.py"])
else:
    print("\n❌ [ACCESS DENIED] Invalid credentials.")