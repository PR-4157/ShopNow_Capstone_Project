import json
import os
import requests

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

with open("reports/weekly-summary.json", "r") as file:
    report = json.load(file)

critical = report["CRITICAL"]
high = report["HIGH"]
medium = report["MEDIUM"]
low = report["LOW"]
images = report["images_scanned"]

# Determine alert level
if critical > 0:
    status = "🚨 CRITICAL ALERT"

elif high > 0:
    status = "⚠ HIGH ALERT"

elif medium > 0:
    status = "⚠ MEDIUM ALERT"

else:
    status = "✅ SECURE"

message = f"""
📅 *Weekly Security Summary*

Images Scanned : {images}

🔴 Critical : {critical}
🟠 High : {high}
🟡 Medium : {medium}
🟢 Low : {low}

Status : {status}
"""

payload = {
    "text": message
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 200:
    print("✅ Slack notification sent successfully.")
else:
    print(f"❌ Failed ({response.status_code})")
    print(response.text)