# Container Image Vulnerability Scanner with Reporting - Sprint-6

## Project Overview

The **Container Image Vulnerability Scanner with Reporting** is a DevSecOps solution designed to automate security scanning of Docker container images before deployment. It integrates vulnerability scanning into CI/CD pipelines using Trivy, generates detailed reports, sends Slack notifications, and provides historical vulnerability tracking through Prometheus and Grafana dashboards.

This project helps organizations identify security issues early in the software development lifecycle and supports secure container deployments.

---

# Features

- Docker image vulnerability scanning using Trivy
- Filesystem security scanning
- Automated scanning in GitHub Actions and Jenkins
- HTML and JSON vulnerability reports
- Slack notifications for scan results
- Prometheus metrics exporter
- Grafana dashboard for historical tracking
- Exception handling for approved vulnerabilities
- Retry mechanism for failed scans
- Report comparison between scans
- Easy deployment using automation scripts

---

# Project Architecture

```
Developer Push
        │
        ▼
GitHub Actions / Jenkins
        │
        ▼
Docker Image Build
        │
        ▼
Trivy Vulnerability Scan
        │
        ▼
Exception Handling
        │
        ▼
Generate Reports
        │
        ▼
Slack Notifications
        │
        ▼
Metrics Exporter
        │
        ▼
Prometheus
        │
        ▼
Grafana Dashboard
        │
        ▼
Historical Tracking
        │
        ▼
Retry & Rescanning
```

---

# Project Structure

```
Image-Scanning-Project/
│
├── shopNow/
│   ├── backend/
│   ├── frontend/
│   └── admin/
│
├── scripts/
│   ├── build.sh
│   ├── scan.sh
│   ├── retry_scan.py
│   ├── exception_handler.py
│   ├── compare_reports.py
│   ├── metrics_exporter.py
│   ├── report_generator.py
│   └── slack_notify.py
│
├── reports/
│   ├── latest/
│   ├── history/
│   └── comparison/
│
├── config/
│   ├── exceptions.yaml
│   ├── approved_vulnerabilities.yaml
│   └── settings.env
│
├── prometheus/
│
├── grafana/
│
├── docs/
│
├── templates/
│
├── .github/
│
├── Jenkinsfile
├── docker-compose.yml
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

---

# Technologies Used

- Docker
- Trivy
- Python
- Bash
- GitHub Actions
- Jenkins
- Prometheus
- Grafana
- Slack Webhook
- YAML
- JSON

---

# Prerequisites

Before running this project, install the following software.

- Docker Desktop
- Git
- Python 3.10+
- Trivy
- Grafana
- Prometheus

---

# Configuration

Update the configuration files.

```
config/approved_vulnerabilities.yaml
```
<img width="2926" height="612" alt="image" src="https://github.com/user-attachments/assets/aa181f90-4aab-4075-a9a0-3e2f9b1d6d9e" />

Example

```yaml
approved:
  - cve: CVE-2026-48758
    reason: Vendor patch pending
    approved_by: Security Team
    review_date: 2026-08-01

  - cve: CVE-2026-33750
    reason: Accepted business risk
    approved_by: DevSecOps Team
    review_date: 2026-09-15
```
<img width="2325" height="336" alt="image" src="https://github.com/user-attachments/assets/8cb9f952-6d04-4f80-8a17-49f5f370bb8a" />

Configure Slack Webhook inside

```
scripts/slack_notify.py
```
<img width="3024" height="224" alt="image" src="https://github.com/user-attachments/assets/1457810a-a9df-46e8-9444-c0c3b7acfe4c" />

---

# Deployment

Run the deployment script.

```bash
chmod +x scripts/setup.sh

./scripts/setup.sh
```
<img width="3023" height="1208" alt="image" src="https://github.com/user-attachments/assets/70c03a60-0d40-40e8-8677-a789c959da3a" />
<img width="3024" height="960" alt="image" src="https://github.com/user-attachments/assets/c926ed6d-32a1-4751-a124-a5d8145564f9" />
<img width="3023" height="1188" alt="image" src="https://github.com/user-attachments/assets/ca158bd7-7520-4fff-95c7-e5e902ec8bf0" />

The deployment script automatically

- Creates required folders
- Builds Docker images
- Starts Prometheus
- Starts Grafana
- Prepares reports directory

---

# Usage

## Build Images

```bash
./scripts/build.sh
```
<img width="3024" height="1845" alt="image" src="https://github.com/user-attachments/assets/052c7c9b-be24-45f5-bc22-6404dfcd3d08" />
<img width="3024" height="1106" alt="image" src="https://github.com/user-attachments/assets/1db7be31-505b-429e-af43-07e4f91a88af" />

---

## Scan Images

```bash
./scripts/scan.sh
```
<img width="3024" height="1564" alt="image" src="https://github.com/user-attachments/assets/5f6e2556-3659-4251-b3f8-da47ed80f67e" />
<img width="3024" height="1827" alt="image" src="https://github.com/user-attachments/assets/9a6b1890-fd91-4503-93a1-db4b8adbbd30" />
<img width="3023" height="1769" alt="image" src="https://github.com/user-attachments/assets/ff6334b7-a49b-4802-8366-ae06b703aca4" />
<img width="3023" height="1850" alt="image" src="https://github.com/user-attachments/assets/57707a89-843d-41a8-b045-c0d82efe7459" />
<img width="3024" height="1855" alt="image" src="https://github.com/user-attachments/assets/9017f3f5-5841-43dc-a0ca-f1e7d0f22b52" />
<img width="3023" height="1819" alt="image" src="https://github.com/user-attachments/assets/415258fc-f614-4bdd-8246-f5811a5bf0d6" />
<img width="3024" height="1865" alt="image" src="https://github.com/user-attachments/assets/671a56cb-3724-49d1-bfe3-bfaef89f4c7a" />

---

## Retry Failed Scan

```bash
python3 scripts/retry_scan.py
```
<img width="2320" height="476" alt="image" src="https://github.com/user-attachments/assets/de59543f-11aa-48df-b30d-aa9a4196386c" />

---

## Compare Reports

```bash
python3 scripts/compare_reports.py
```
<img width="3024" height="506" alt="image" src="https://github.com/user-attachments/assets/c366724c-3789-49bf-a405-e4ddd4ac69e3" />

---

## Generate HTML Report

```bash
python3 scripts/report_generator.py
```
<img width="2318" height="701" alt="image" src="https://github.com/user-attachments/assets/423477ed-36d7-4284-9007-d73bd3301ce5" />

---

# 📊 Reports

Generated reports are stored inside

Supported report formats

- JSON
- HTML
- PDF

<img width="2322" height="988" alt="image" src="https://github.com/user-attachments/assets/c38ba3b9-8b4e-4aa1-b2b3-2e8f7c33f259" />
<img width="1161" height="494" alt="Screenshot 2026-07-28 at 7 41 28 PM" src="https://github.com/user-attachments/assets/7d3d2c56-2f11-4fdb-8f44-7276cdf9625d" />

---

# 📈 Grafana Dashboard

Open browser
```
Prometheus:
http://localhost:9090/query

Grafana:
http://localhost:3002
```
---

# 🔄 CI/CD Integration

## GitHub Actions

Pipeline automatically

- Builds Docker Images
- Runs Trivy Scan
- Generates Reports
- Uploads Reports
- Sends Slack Notification

Workflow file

```
.github/workflows/security-pipeline.yml
```
<img width="2320" height="652" alt="image" src="https://github.com/user-attachments/assets/e85e4c44-3743-4e7d-8091-c9bd50303e80" />

---

## Jenkins

Pipeline stages

- Checkout
- Build
- Scan
- Generate Reports
- Notifications

Pipeline file

```
Jenkinsfile
```
<img width="2315" height="1484" alt="image" src="https://github.com/user-attachments/assets/5b6fab2a-03ec-4efa-8e7b-d5ec0fe452d9" />

---

# 🧪 Testing

The project has been tested on

| Test | Status |
|------|--------|
| Docker Build | ✅ |
| Trivy Scan | ✅ |
| GitHub Actions | ✅ |
| Jenkins Pipeline | ✅ |
| Slack Notification | ✅ |
| Grafana Dashboard | ✅ |
| Exception Handling | ✅ |
| Retry Logic | ✅ |

---

# 📸 Screenshots

<img width="3023" height="1035" alt="image" src="https://github.com/user-attachments/assets/abd34c64-76a6-4e63-99a6-65db6be79e1b" />

<img width="3024" height="784" alt="image" src="https://github.com/user-attachments/assets/b1c9e88e-3e76-49f4-9292-f93d4d2f5a5c" />


```
docs/screenshots/

dashboard.png

slack-alert.png

github-actions.png

jenkins-build.png
```

---

## Slack notification not working

Verify Slack Webhook URL: 
https://app.slack.com/client/T0BHAHJQ6BD/D0BHLJPLGE8

---

## Grafana dashboard 

Check Prometheus targets.
http://localhost:3002/d/adc5tp8/shopnow-security-dashboard?orgId=1&from=2026-07-26T11:14:34.114Z&to=2026-07-26T11:44:34.114Z&timezone=browser&var-filter0=&var-query0=&var-image=backend&var-severity=HIGH&dtab=New-tab

---

# 🔮 Future Improvements

- Docker Scout integration
- Microsoft Teams notifications
- Email alerts
- Kubernetes support
- Multi-cloud deployment
- AI-based vulnerability prioritization

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository, create a feature branch, and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Rahulkumar Prajapati

Master of Science in Information Technology

DevSecOps Capstone Project

Hero Vired

---

# 🙏 Acknowledgements

- Aqua Security (Trivy)
- Docker
- Grafana Labs
- Prometheus
- GitHub Actions
- Jenkins Community
- Hero Vired
