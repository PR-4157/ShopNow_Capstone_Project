# Container Image Vulnerability Scanner with Reporting – Sprint 2

## Overview

Sprint 2 extends the Sprint 1 implementation by automating Docker image vulnerability scanning using CI/CD pipelines.

Instead of manually building Docker images and scanning them with Trivy, the process is automated using GitHub Actions and Jenkins.

Whenever code is pushed to the repository, the pipeline:

- Builds Docker images
- Scans images using Trivy
- Generates vulnerability reports
- Fails the pipeline if HIGH or CRITICAL vulnerabilities are detected

---

# Sprint 2 Objectives

- Automate Docker image builds
- Automate Trivy image scanning
- Configure environment-based scanning
- Integrate with GitHub Actions
- Integrate with Jenkins
- Define build pass/fail rules
- Generate security reports automatically

---

# CI/CD Workflow

```text
Developer Pushes Code
        │
        ▼
GitHub Actions / Jenkins
        │
        ▼
Checkout Repository
        │
        ▼
Build Docker Images
        │
        ▼
Run Trivy Scan
        │
        ▼
Generate JSON Reports
        │
        ▼
HIGH / CRITICAL Vulnerabilities?
       │
 ┌─────┴─────┐
 │           │
 ▼           ▼
Fail       Pass
Pipeline   Pipeline
```

---

# Technologies Used

| Tool | Purpose |
|------|---------|
| Docker | Build container images |
| Trivy | Vulnerability scanner |
| GitHub Actions | CI/CD automation |
| Jenkins | CI/CD pipeline |
| Bash | Automation scripts |
| JSON | Scan reports |
| Git | Version control |

---

# Project Structure

```text
container-vulnerability-scanner/
│
├── shopNow/
│   ├── backend/
│   ├── frontend/
│   ├── admin/
│
├── scripts/
│   ├── build.sh
│   └── scan.sh
│
├── reports/
│   ├── backend-report.json
│   ├── frontend-report.json
│   ├── admin-report.json
│   ├── nginx-report.json
│   ├── python-report.json
│   └── ubuntu-report.json
│
├── .github/
│   └── workflows/
│       └── security-pipeline.yml
│
├── Jenkinsfile
├── .env
└── README.md
```
<img width="1512" height="801" alt="Screenshot 2026-07-08 at 6 54 27 PM" src="https://github.com/user-attachments/assets/1bb7386a-a7d8-42f4-9a48-7e5385b22021" />

---

# Environment Configuration

Create a `.env` file in the project root.

```text
# Trivy Scan Configuration
SEVERITY=HIGH,CRITICAL
TRIVY_FORMAT=json
REPORTS_DIR=reports

# Docker Image Names
BACKEND_IMAGE=shopnow-backend:v1
FRONTEND_IMAGE=shopnow-frontend:v1
ADMIN_IMAGE=shopnow-admin:v1
```
<img width="1512" height="309" alt="Screenshot 2026-07-07 at 7 16 27 PM" src="https://github.com/user-attachments/assets/3c9d2ed0-d748-4140-b257-d06f24ca1a19" />
VS Code:
<img width="1756" height="690" alt="image" src="https://github.com/user-attachments/assets/e46c0eec-63e0-44fe-9c8b-52c4aba2cbeb" />

---

# Automated Docker Build

Run:

```bash
chmod +x scripts/build.sh
./scripts/build.sh
```
The script builds all ShopNow Docker images:
- Backend
- Frontend
- Admin
<img width="1512" height="573" alt="B - 1" src="https://github.com/user-attachments/assets/680160db-c8da-484e-96ac-0ca730ea4e43" />
<img width="1512" height="478" alt="B - 2" src="https://github.com/user-attachments/assets/5b7c9e0e-644f-40c9-b201-a946f368a151" />
<img width="1512" height="526" alt="B - 3" src="https://github.com/user-attachments/assets/701cfa52-d78a-435a-9e82-36183b113e46" />
VS Code:
<img width="876" height="588" alt="B " src="https://github.com/user-attachments/assets/27462c80-e56d-4927-9885-fb64ece28b19" />

---

# Automated Trivy Scan

Run:

```bash
chmod +x scripts/scan.sh
./scripts/scan.sh
```
The script:
- Loads configuration from `.env`
- Scans all Docker images
- Generates JSON reports
- Uses the configured severity threshold
<img width="1512" height="781" alt="S - 1" src="https://github.com/user-attachments/assets/a78a8861-81f1-43ac-b099-f8f31e659a51" />
<img width="1512" height="911" alt="S - 2" src="https://github.com/user-attachments/assets/9cf2e36b-b387-4acf-abef-925c63f57fca" />
<img width="1512" height="909" alt="S - 3" src="https://github.com/user-attachments/assets/0c6f2564-e6a6-478a-b456-fbde9ca524b6" />
<img width="1512" height="911" alt="S - 4" src="https://github.com/user-attachments/assets/acb84915-0d5a-4d8f-bb08-3c7931e288f0" />
<img width="1512" height="897" alt="S - 5" src="https://github.com/user-attachments/assets/bedd782f-e42a-4194-a74c-6b7cf7ba4f92" />
<img width="1512" height="910" alt="S - 6" src="https://github.com/user-attachments/assets/ab1f2e74-6e4b-4c6d-bb39-b3d6757f9fd4" />
<img width="1512" height="896" alt="S - 7" src="https://github.com/user-attachments/assets/179e4abd-e9a8-4dc3-b191-dad4486d9a31" />
<img width="1512" height="897" alt="S - 8" src="https://github.com/user-attachments/assets/77a25a6a-4a85-45cc-aed3-bb000a85d643" />
<img width="1512" height="913" alt="S - 9" src="https://github.com/user-attachments/assets/5cb92818-8ff7-4e90-a540-7597ec9c1f08" />
<img width="1512" height="911" alt="S - 10" src="https://github.com/user-attachments/assets/67161098-f604-4977-aaa8-c84403236482" />
<img width="1512" height="897" alt="S - 11" src="https://github.com/user-attachments/assets/0775a878-b7af-4bff-ae7b-7d0500d87fa7" />
<img width="1512" height="525" alt="S - 12" src="https://github.com/user-attachments/assets/ea177c0a-bdd7-463e-828f-d0c9d4fa00d1" />
<img width="1512" height="891" alt="S - 13" src="https://github.com/user-attachments/assets/a96514f8-bf51-4e8e-be7f-79c97067fee9" />
<img width="1511" height="724" alt="S - 14" src="https://github.com/user-attachments/assets/231c51ae-f9e5-4b3d-8bb0-70500bbcaaa7" />
<img width="1507" height="432" alt="S - 15" src="https://github.com/user-attachments/assets/33b40122-d9f1-47ec-ad43-7986125855e1" />
VS Code:
<img width="874" height="526" alt="Screenshot 2026-07-09 at 9 01 16 PM" src="https://github.com/user-attachments/assets/381ed935-0321-4b59-a9fd-ce27f36fc5ac" />
<img width="873" height="602" alt="Screenshot 2026-07-09 at 9 01 06 PM" src="https://github.com/user-attachments/assets/86de46a4-30cb-47bf-9fcc-8c7575613069" />

---

# Generated Reports

```text
reports/
├── backend-report.json
├── frontend-report.json
├── admin-report.json
├── nginx-report.json
├── python-report.json
└── ubuntu-report.json
```
<img width="1512" height="197" alt="Screenshot 2026-07-09 at 9 12 52 PM" src="https://github.com/user-attachments/assets/d9278b0b-2862-4cf4-8180-90c2fd5a4659" />

---

# GitHub Actions Pipeline

The GitHub Actions workflow is located at:

```text
.github/workflows/security-pipeline.yml
```
<img width="1512" height="857" alt="SP - 1" src="https://github.com/user-attachments/assets/348f0e0a-62d8-47ec-8ee9-8b5fae8cfd61" />

Pipeline stages:

1. Checkout repository
2. Set up Docker
3. Install Trivy
4. Build Docker images
5. Scan images
6. Upload reports
7. Pass or fail the workflow

The workflow runs automatically on every push to the configured branch.

---

# Jenkins Pipeline

The Jenkins pipeline is defined in:

```text
Jenkinsfile
```
<img width="3024" height="480" alt="image" src="https://github.com/user-attachments/assets/39d52a36-9864-49eb-b4b7-821c436cf7d6" />

Pipeline stages:

```text
Checkout Code
      │
      ▼
Build Images
      │
      ▼
Trivy Scan
      │
      ▼
Archive Reports
      │
      ▼
Pass / Fail
```

---

# Pass / Fail Criteria

The pipeline blocks insecure images.

| Severity | Pipeline Result |
|----------|-----------------|
| LOW | Pass |
| MEDIUM | Pass |
| HIGH | Fail |
| CRITICAL | Fail |

This is enforced using Trivy's exit code functionality.

---

# Testing

The automation was validated using the following images:

| Image | Purpose |
|------|---------|
| ShopNow Backend | Application scan |
| ShopNow Frontend | Application scan |
| ShopNow Admin | Application scan |
| nginx | Sample image |
| python | Sample image |
| ubuntu | Sample image |

---

# Sprint 2 Deliverables

| Deliverable | Status |
|-------------|--------|
| Docker build automation | ✅ |
| Trivy scan automation | ✅ |
| Environment configuration | ✅ |
| GitHub Actions integration | ✅ |
| Jenkins integration | ✅ |
| Pass/Fail rules | ✅ |
| Automated JSON reports | ✅ |

---

# Screenshots

Suggested screenshots:

```text
screenshots/
├── github-actions-success.png
├── github-actions-failed.png
├── jenkins-pipeline.png
├── trivy-scan.png
├── docker-images.png
└── reports-folder.png
```

Example:

```markdown
## GitHub Actions

![GitHub Actions](screenshots/github-actions-success.png)

## Jenkins Pipeline

![Jenkins](screenshots/jenkins-pipeline.png)

## Trivy Scan

![Trivy Scan](screenshots/trivy-scan.png)
```

---

# Future Enhancements

Planned improvements for the next sprint include:

- HTML vulnerability reports
- Slack or Microsoft Teams notifications
- Dashboard for vulnerability history
- Docker Scout integration
- SonarQube integration
- GitLeaks secret scanning
- Multi-branch pipeline support

---

# Author

**Rahulkumar Prajapati**

DevSecOps Capstone Project

---

# License

This project is intended for educational purposes as part of a DevSecOps Capstone Project.
