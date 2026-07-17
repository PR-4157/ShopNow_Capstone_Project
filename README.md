# Sprint 4 – Web Dashboard for Historical Vulnerability Tracking

## Project Overview

Sprint 4 completes the **Container Image Vulnerability Scanner with Reporting** project by introducing a web-based dashboard for monitoring vulnerability trends over time.

The solution integrates **Docker**, **Trivy**, **GitHub Actions**, **Jenkins**, **Prometheus**, and **Grafana** to automate vulnerability scanning, export security metrics, and visualize historical data through an interactive dashboard. This enables developers and security teams to track vulnerabilities, analyze trends, and monitor the security posture of container images.

---

# Sprint Goal

Provide a user-friendly dashboard that tracks vulnerability history and enables trend analysis by visualizing security metrics collected from automated container image scans.

---

# Objectives

- Set up Grafana for dashboard visualization.
- Configure Prometheus to collect vulnerability metrics.
- Export scan results as Prometheus metrics.
- Visualize historical vulnerability trends.
- Implement dashboard filters for images, severity, and date ranges.
- Validate dashboard functionality and responsiveness.

---

# System Architecture

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
Trivy Vulnerability Scan
          │
          ▼
Generate JSON Reports
          │
          ▼
Metrics Exporter (Python)
          │
          ▼
Prometheus
          │
          ▼
Grafana Dashboard
          │
          ▼
Historical Vulnerability Tracking
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Docker | Containerization |
| Trivy | Vulnerability Scanning |
| Python | Metrics Exporter |
| Prometheus | Metrics Collection |
| Grafana | Dashboard Visualization |
| GitHub Actions | CI/CD Automation |
| Jenkins | CI/CD Pipeline |

---

# Project Structure

```text
container-vulnerability-scanner/
│
├── backend/
├── frontend/
├── admin/
│
├── reports/
│   ├── backend-report.json
│   ├── frontend-report.json
│   ├── admin-report.json
│   └── ...
│
├── scripts/
│   ├── build.sh
│   ├── scan.sh
│   ├── slack_notify.py
│   └── metrics_exporter.py
│
├── prometheus/
│   └── prometheus.yml
│
├── grafana/
│   ├── dashboards/
│   └── provisioning/
│
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```
<img width="3021" height="1212" alt="image" src="https://github.com/user-attachments/assets/55bf7743-3a5e-4bf9-837b-157b74273b77" />
<img width="3024" height="847" alt="image" src="https://github.com/user-attachments/assets/482a82d5-68c1-40fe-86c7-eb96876b7c3b" />

---

# Features

## Historical Vulnerability Dashboard

Visualize vulnerability trends using Grafana.

Dashboard displays:

- Total Images Scanned
- Critical Vulnerabilities
- High Vulnerabilities
- Medium Vulnerabilities
- Low Vulnerabilities
- Vulnerability Trends Over Time

---

## Prometheus Metrics Collection

Prometheus collects metrics exported from Trivy scan results.

Example metrics:

```text
shopnow_images_scanned 3

shopnow_vulnerabilities{image="backend",severity="CRITICAL"} 2
shopnow_vulnerabilities{image="backend",severity="HIGH"} 29
shopnow_vulnerabilities{image="frontend",severity="HIGH"} 11
shopnow_vulnerabilities{image="admin",severity="LOW"} 28
```

---

## Grafana Dashboard Panels

The dashboard includes:

- Total Images Scanned
- Critical Vulnerabilities
- High Vulnerabilities
- Medium Vulnerabilities
- Low Vulnerabilities
- Vulnerability Trend Graph
- Scan History

---

## Dashboard Filters

Users can filter dashboard data by:

### Image Name

- Backend
- Frontend
- Admin

### Severity

- LOW
- MEDIUM
- HIGH
- CRITICAL

### Date Range

- Today
- Last 7 Days
- Last 30 Days
- Custom Range

---

## Historical Trend Analysis

Track how vulnerabilities change over time.

Example:

```text
Week 1

Critical : 6

Week 2

Critical : 4

Week 3

Critical : 2

Week 4

Critical : 0
```

This helps identify whether the security posture is improving.

---

# Running the Dashboard

## Start Prometheus

```bash
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v $(pwd)/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```
<img width="3024" height="1063" alt="image" src="https://github.com/user-attachments/assets/288e853d-6a22-44e4-b4e2-1cbf4bc219b5" />

---

## Start Grafana

```bash
docker run -d \
  --name grafana \
  -p 3002:3000 \
  grafana/grafana
```
<img width="3024" height="557" alt="image" src="https://github.com/user-attachments/assets/06f519ee-35ce-4ae9-847b-084a159cf0e3" />
<img width="3024" height="600" alt="image" src="https://github.com/user-attachments/assets/3b18b2d2-ab14-4a5b-a0fa-516645915a75" />

---

## Start the Metrics Exporter

```bash
python metrics_exporter.py
```
<img width="2494" height="556" alt="image" src="https://github.com/user-attachments/assets/e89d747e-a616-4ffa-ab8e-ff10455da114" />

---

## Open Services

| Service | URL |
|----------|-----|
| Metrics Exporter | http://localhost:8000/metrics |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3002 |

---

# Dashboard Overview

The Grafana dashboard provides:

- Security Overview
- Images Scanned
- Vulnerability Distribution
- Historical Trends
- Severity Breakdown
- Recent Scan Results

---

# Sample Metrics

```text
images_scanned 5

critical_vulnerabilities 2

high_vulnerabilities 8

medium_vulnerabilities 14

low_vulnerabilities 27
```

---

# Screenshots

## Grafana Dashboard

<img width="3024" height="1731" alt="image" src="https://github.com/user-attachments/assets/5382e777-bfa2-452f-b966-7dc727082b7c" />
<img width="1040" height="606" alt="Screenshot 2026-07-17 at 7 23 12 PM" src="https://github.com/user-attachments/assets/3a6882d3-0b72-4631-a9ad-3e14905c4be5" />
<img width="1512" height="576" alt="Screenshot 2026-07-17 at 5 14 24 PM" src="https://github.com/user-attachments/assets/5280b929-bb04-4052-8324-ad49d6f4df09" />
<img width="1215" height="523" alt="Screenshot 2026-07-17 at 5 14 35 PM" src="https://github.com/user-attachments/assets/fc0da92f-8cca-4cf6-ac3c-2eb3c2f90dab" />

## Prometheus Targets

<img width="1512" height="608" alt="Screenshot 2026-07-17 at 5 12 41 PM" src="https://github.com/user-attachments/assets/1d31adff-d3eb-4d1a-91d0-2fc05b9fe79d" />

## Vulnerability Trends

<img width="3023" height="1568" alt="image" src="https://github.com/user-attachments/assets/fc7befd1-8ef0-4bae-8ee6-289d4993d92e" />

<img width="1512" height="690" alt="Screenshot 2026-07-16 at 6 46 57 PM" src="https://github.com/user-attachments/assets/c62c49e6-c33e-46e4-881f-c171167e9cd3" />
<img width="2244" height="1330" alt="image" src="https://github.com/user-attachments/assets/3d45144f-6aac-4201-b635-893acd46cefa" />
<img width="2246" height="990" alt="image" src="https://github.com/user-attachments/assets/0da78379-a0ad-4444-ab57-f4c1a80e6fe8" />
<img width="2116" height="1506" alt="image" src="https://github.com/user-attachments/assets/0da4ee0e-b62e-4e2d-9063-e56a8d9d401a" />
<img width="912" height="838" alt="Screenshot 2026-07-16 at 7 21 28 PM" src="https://github.com/user-attachments/assets/5b095ddb-32df-47f5-ac82-d7af34c8c078" />
<img width="3024" height="700" alt="image" src="https://github.com/user-attachments/assets/0d691cf8-3a30-4d9e-87af-7511fee98df0" />

---

# Testing

The dashboard was tested by:

- Running multiple Trivy scans.
- Exporting vulnerability metrics.
- Verifying Prometheus successfully collected metrics.
- Confirming Grafana displayed historical trends.
- Testing filters for image name, severity, and date range.
- Ensuring dashboard updates after new scans.

---

# Sprint 4 Deliverables

| Deliverable | Status |
|-------------|--------|
| Metrics Exporter | ✅ |
| Prometheus Configuration | ✅ |
| Grafana Dashboard | ✅ |
| Historical Trend Tracking | ✅ |
| Dashboard Filters | ✅ |
| Vulnerability Charts | ✅ |
| Dashboard Testing | ✅ |

---

# Final Outcome

Sprint 4 completes the DevSecOps pipeline by adding continuous monitoring and visualization. Vulnerability data collected during automated container image scans is exported to Prometheus and displayed in Grafana, allowing teams to monitor security trends, analyze historical data, and quickly identify high-risk container images.

---

# 👨‍💻 Author

**Rahulkumar Prajapati**

DevSecOps Capstone Project

---

# 📄 License

This project is developed for educational purposes as part of a DevSecOps Capstone Project.
