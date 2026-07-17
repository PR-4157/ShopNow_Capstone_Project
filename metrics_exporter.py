import json
import time

from prometheus_client import Gauge, start_http_server

# Metric with image label
vulnerabilities = Gauge(
    "shopnow_vulnerabilities",
    "Container vulnerabilities",
    ["image", "severity"]
)

images_scanned = Gauge(
    "shopnow_images_scanned",
    "Images scanned"
)

REPORTS = {
    "backend": "reports/backend-report.json",
    "frontend": "reports/frontend-report.json",
    "admin": "reports/admin-report.json"
}

start_http_server(8000)

print("Metrics server running on http://localhost:8000/metrics")

while True:

    images_scanned.set(len(REPORTS))

    for image_name, filename in REPORTS.items():

        counts = {
            "CRITICAL": 0,
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0
        }

        try:
            with open(filename) as f:
                report = json.load(f)

            for result in report.get("Results", []):

                for vuln in result.get("Vulnerabilities", []):

                    severity = vuln.get("Severity")

                    if severity in counts:
                        counts[severity] += 1

        except FileNotFoundError:
            print(f"Missing report: {filename}")
            continue

        for severity, count in counts.items():
            vulnerabilities.labels(
                image=image_name,
                severity=severity
            ).set(count)

    time.sleep(15)