import json
from jinja2 import Environment, FileSystemLoader

# Read Trivy report
with open("reports/backend-report.json", "r") as file:
    report = json.load(file)

critical = 0
high = 0
medium = 0
low = 0

for result in report.get("Results", []):

    for vuln in result.get("Vulnerabilities", []):

        severity = vuln.get("Severity")

        if severity == "CRITICAL":
            critical += 1

        elif severity == "HIGH":
            high += 1

        elif severity == "MEDIUM":
            medium += 1

        elif severity == "LOW":
            low += 1

env = Environment(loader=FileSystemLoader("templates"))

template = env.get_template("report_template.html")

html = template.render(
    image="shopnow-backend:v1",
    critical=critical,
    high=high,
    medium=medium,
    low=low
)

with open("reports/backend-report.html", "w") as file:
    file.write(html)

print("HTML Report Generated Successfully!")