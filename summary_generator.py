import json
import os

# Trivy report files
REPORTS = [
    "backend-report.json",
    "frontend-report.json",
    "admin-report.json"
]

summary = {
    "images_scanned": 0,
    "CRITICAL": 0,
    "HIGH": 0,
    "MEDIUM": 0,
    "LOW": 0
}

# Read every report
for filename in REPORTS:

    path = os.path.join("reports", filename)

    if not os.path.exists(path):
        print(f"{filename} not found")
        continue

    summary["images_scanned"] += 1

    with open(path, "r") as f:
        report = json.load(f)

    for result in report.get("Results", []):

        vulnerabilities = result.get("Vulnerabilities", [])

        if vulnerabilities is None:
            continue

        for vuln in vulnerabilities:

            severity = vuln.get("Severity")

            if severity in summary:
                summary[severity] += 1

# Save weekly summary
output = "reports/weekly-summary.json"

with open(output, "w") as outfile:
    json.dump(summary, outfile, indent=4)

print("Weekly summary generated successfully!")
print(summary)