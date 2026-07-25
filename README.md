<img width="2926" height="1700" alt="image" src="https://github.com/user-attachments/assets/8ee6250e-4516-41c4-bc4a-07a3655bdde3" /># Sprint 5 – Advanced Scanner Customization and Exception Handling

## Project Overview

Sprint 5 is the final stage of the **Container Image Vulnerability Scanner with Reporting** capstone project. This sprint enhances the vulnerability scanner with enterprise-inspired features that improve flexibility, reliability, and maintainability.

The scanner now supports:

* Vulnerability exception handling
* Automatic rescanning of container images
* Retry logic for temporary scan failures
* User-friendly error handling
* Approved vulnerability tracking for audit purposes

These features simulate how modern DevSecOps teams manage container security in production environments.

---

# Sprint Goal

Develop an intelligent vulnerability scanning solution that supports approved vulnerability exceptions, rescanning, retry mechanisms, and audit tracking while integrating seamlessly into the CI/CD pipeline.

---

# Sprint Features

## Vulnerability Exception Handling

Approved vulnerabilities can be excluded from pipeline failure by maintaining an exception list.

Example:

```yaml
approved:
  - cve: CVE-2026-48758
    reason: Vendor patch pending
    approved_by: Security Team
    review_date: "2026-08-01"

  - cve: CVE-2026-33750
    reason: Accepted business risk
    approved_by: DevSecOps Team
    review_date: "2026-09-15"
```
<img width="2247" height="1035" alt="image" src="https://github.com/user-attachments/assets/133d5976-26ed-4d6d-9e4c-89437aadd29c" />

Workflow:

```text
Trivy Scan
      │
      ▼
Read Exception List
      │
      ▼
Approved?
 ┌────┴────┐
 │         │
Yes        No
 │         │
 ▼         ▼
Ignore   Report Normally
```

Approved vulnerabilities remain visible in reports but do not fail the build.

---

## ✅ Automatic Rescanning

The scanner can perform a new vulnerability scan after rebuilding the image or updating dependencies.

Workflow:

```text
Docker Image
      │
      ▼
Initial Scan
      │
      ▼
Save Report
      │
      ▼
Update Image
      │
      ▼
Rescan
      │
      ▼
Compare Reports
```

Historical reports are stored for trend analysis.

Example:

```text
reports/history/

backend-v1.json

backend-v2.json
```

---

## ✅ Report Comparison

The project compares previous and current scan reports to measure security improvements.

Example output:

```text
Previous Scan

CRITICAL : 2
HIGH : 5
MEDIUM : 10

Current Scan

CRITICAL : 0
HIGH : 2
MEDIUM : 7

Security Improvement

CRITICAL : -2
HIGH : -3
MEDIUM : -3
```

---

## ✅ Retry Logic

Temporary scan failures are automatically retried before the pipeline fails.

Workflow:

```text
Start Scan
     │
     ▼
Success?
     │
 ┌───┴────┐
 │        │
Yes       No
 │        │
 ▼        ▼
Finish   Retry 1
           │
           ▼
       Retry 2
           │
           ▼
       Retry 3
           │
           ▼
      Still Failed?
           │
      Pipeline Fails
```

This improves the reliability of CI/CD pipelines.

---

## ✅ Error Handling

The scanner performs prerequisite checks before executing a scan.

Examples:

### Docker Not Running

```text
Docker daemon is not running.
Start Docker Desktop and rerun the pipeline.
```

### Trivy Missing

```text
Trivy is not installed.
Install Trivy and try again.
```

### Docker Image Missing

```text
Specified Docker image was not found.
Build the image before running the scan.
```

These messages help users resolve common issues quickly.

---

## ✅ Approved Vulnerability Tracking

Approved vulnerabilities are tracked for auditing instead of being removed completely.

Example record:

| Field       | Value                |
| ----------- | -------------------- |
| CVE         | CVE-2025-11111       |
| Severity    | HIGH                 |
| Reason      | Vendor patch pending |
| Approved By | Security Team        |
| Review Date | 2026-08-01           |

This creates a clear audit trail of accepted security risks.

---

# 🏗️ System Architecture

```text
Developer Pushes Code
          │
          ▼
GitHub Actions / Jenkins
          │
          ▼
Build Docker Images
          │
          ▼
Trivy Scan
          │
          ▼
Exception Handler
          │
     ┌────┴─────┐
     │          │
 Approved    Unapproved
     │          │
     ▼          ▼
Ignore      Include in Report
     │
     ▼
Generate Reports
     │
     ▼
Slack Notifications
     │
     ▼
Export Metrics
     │
     ▼
Prometheus
     │
     ▼
Grafana Dashboard
     │
     ▼
Historical Trend Analysis
```

---

# 🛠️ Technologies Used

| Technology     | Purpose                 |
| -------------- | ----------------------- |
| Docker         | Containerization        |
| Trivy          | Vulnerability scanning  |
| Python         | Automation scripts      |
| YAML           | Exception configuration |
| GitHub Actions | CI/CD automation        |
| Jenkins        | Continuous Integration  |
| Prometheus     | Metrics collection      |
| Grafana        | Dashboard visualization |

---

# 📂 Project Structure

```text
Image-Scanning-Project/
│
├── config/
│   ├── exceptions.yaml
│   ├── approved_vulnerabilities.yaml
│   └── settings.env
│
├── reports/
│   ├── history/
│   ├── latest/
│   ├── comparison/
│   └── ...
│
├── scripts/
│   ├── build.sh
│   ├── scan.sh
│   ├── exception_handler.py
│   ├── rescan.py
│   ├── compare_reports.py
│   ├── retry_scan.py
│   ├── report_generator.py
│   └── slack_notify.py
│
├── prometheus/
├── grafana/
├── Jenkinsfile
├── docker-compose.yml
└── README.md
```

---

# ▶️ How to Run

Build the Docker image:

```bash
./scripts/build.sh
```
<img width="3021" height="1856" alt="image" src="https://github.com/user-attachments/assets/a8a6d389-78cc-4342-b5c5-fec59889077d" />
<img width="3024" height="1109" alt="image" src="https://github.com/user-attachments/assets/ceaa19b4-d025-4d05-b4e6-6fc56017e3c0" />

Run the vulnerability scan:

```bash
./scripts/scan.sh
```
<img width="3024" height="1846" alt="image" src="https://github.com/user-attachments/assets/9f734fc8-f0bc-4438-b72f-066734bbda43" />
<img width="3023" height="1870" alt="image" src="https://github.com/user-attachments/assets/8ef644a4-12c4-4f77-9415-4db8f1299695" />
<img width="3024" height="1872" alt="image" src="https://github.com/user-attachments/assets/734f194a-efa5-440f-9bfe-aab8857db3f3" />
<img width="3024" height="1806" alt="image" src="https://github.com/user-attachments/assets/968f260a-e10e-4a17-ba64-aac9171fbd0a" />
<img width="3024" height="830" alt="image" src="https://github.com/user-attachments/assets/f81c5801-9351-4f90-8207-2fbec323449b" />

Process approved exceptions:

```bash
python scripts/exception_handler.py
```
<img width="3024" height="817" alt="image" src="https://github.com/user-attachments/assets/21537b05-ed61-463a-a85b-ef0d91d71882" />

Run a rescan:

```bash
python scripts/rescan.py
```
<img width="3024" height="532" alt="image" src="https://github.com/user-attachments/assets/141c7742-ae95-4242-8050-1e0e52ef4729" />

Compare reports:

```bash
python scripts/compare_reports.py
```
<img width="3024" height="506" alt="image" src="https://github.com/user-attachments/assets/2225d9f0-f550-4852-a558-0b4e6c9ade95" />

Run the retry-enabled scan:

```bash
python scripts/retry_scan.py
```
<img width="3024" height="514" alt="image" src="https://github.com/user-attachments/assets/90191070-4e4c-43ce-b823-7672037a8410" />

---

# 🧪 Testing

The Sprint 5 implementation was tested to verify:

* Approved CVEs are excluded from pass/fail evaluation.
* Approved vulnerabilities remain visible in audit reports.
* Historical reports are stored correctly.
* Report comparison identifies vulnerability changes.
* Retry logic successfully handles temporary failures.
* Error handling displays clear and actionable messages.

---

# 📸 Screenshots

Include screenshots of:

* Exception Handling Output
* Approved Vulnerability Report
* Rescan Results
* Report Comparison
* Retry Logic Execution
* Grafana Dashboard
* GitHub Actions or Jenkins Pipeline

Example folder:

exception-handler.png
<img width="2926" height="1700" alt="image" src="https://github.com/user-attachments/assets/9613b7d3-c81c-44f4-92a8-f7f36c067bc8" />
<img width="1462" height="546" alt="Screenshot 2026-07-25 at 3 56 25 PM" src="https://github.com/user-attachments/assets/7110a1a0-c58f-494e-a52a-cc3916d0ce1b" />

approved-vulnerabilities.png
<img width="2247" height="1035" alt="image" src="https://github.com/user-attachments/assets/f9ac5073-e1a3-4c39-bcb4-7591f74794a2" />

rescan-results.png

report-comparison.png

retry-scan.png

grafana-dashboard.png

github-actions.png

---

# 📦 Sprint 5 Deliverables

| Deliverable                            | Status |
| -------------------------------------- | ------ |
| `config/exceptions.yaml`               | ✅      |
| `config/approved_vulnerabilities.yaml` | ✅      |
| Exception Handling Logic               | ✅      |
| Rescan Functionality                   | ✅      |
| Report Comparison                      | ✅      |
| Retry Logic                            | ✅      |
| Error Handling                         | ✅      |
| Approved Vulnerability Tracking        | ✅      |

---

# 🎯 Conclusion

Sprint 5 completes the DevSecOps capstone by adding enterprise-inspired vulnerability management capabilities. The project now supports automated container scanning, CI/CD integration, reporting, notifications, monitoring dashboards, exception management, rescanning, retry mechanisms, and approved vulnerability tracking.

This end-to-end workflow demonstrates a practical DevSecOps solution that aligns with modern container security practices while remaining suitable for an academic capstone project.

