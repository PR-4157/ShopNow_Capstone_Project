import json

# Previous scan report
OLD_REPORT = "reports/history/backend-v1.json"

# Current scan report
NEW_REPORT = "reports/history/backend-v2.json"


def count_vulnerabilities(report_file):
    counts = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0
    }

    with open(report_file, "r") as file:
        data = json.load(file)

    results = data.get("Results", [])

    for result in results:
        vulnerabilities = result.get("Vulnerabilities", [])

        for vuln in vulnerabilities:
            severity = vuln.get("Severity")

            if severity in counts:
                counts[severity] += 1

    return counts


old_counts = count_vulnerabilities(OLD_REPORT)
new_counts = count_vulnerabilities(NEW_REPORT)

print("Previous Scan")
print(old_counts)

print("\nCurrent Scan")
print(new_counts)

print("Previous Scan")
print(old_counts)

print("\nCurrent Scan")
print(new_counts)

print("\nSecurity Improvement")

for severity in old_counts:
    diff = new_counts[severity] - old_counts[severity]

    if diff < 0:
        print(f"{severity}: Improved ({abs(diff)} fewer vulnerabilities)")
    elif diff > 0:
        print(f"{severity}: Increased ({diff} more vulnerabilities)")
    else:
        print(f"{severity}: No change")