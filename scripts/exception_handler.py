import json
import yaml

# Load approved vulnerabilities
with open("config/approved_vulnerabilities.yaml", "r") as file:
    data = yaml.safe_load(file)

approved = data["approved"]

# Load Trivy report
REPORT = "reports/history/backend-v2.json"

with open(REPORT, "r") as file:
    report = json.load(file)

# Create lookup dictionary
approved_lookup = {}

for item in approved:
    approved_lookup[item["cve"]] = item

# Audit report file
AUDIT_REPORT = "reports/approved_vulnerabilities.txt"

with open(AUDIT_REPORT, "w") as audit_file:

    audit_file.write("Approved Vulnerabilities\n")
    audit_file.write("------------------------\n\n")

    print("Checking vulnerabilities...\n")

    # Compare vulnerabilities
    for result in report.get("Results", []):
        vulnerabilities = result.get("Vulnerabilities", [])

        for vulnerability in vulnerabilities:

            cve = vulnerability.get("VulnerabilityID")

            if cve in approved_lookup:

                info = approved_lookup[cve]

                print(f"""
✅ Approved CVE : {cve}
Reason          : {info['reason']}
Approved By     : {info['approved_by']}
Review Date     : {info['review_date']}
""")

                # Write to audit report
                audit_file.write(f"CVE: {cve}\n")
                audit_file.write(f"Reason: {info['reason']}\n")
                audit_file.write(f"Approved By: {info['approved_by']}\n")
                audit_file.write(f"Review Date: {info['review_date']}\n")
                audit_file.write("-" * 40 + "\n")

            else:
                print(f"❌ Report: {cve}")

print(f"\n✅ Audit report saved to {AUDIT_REPORT}")