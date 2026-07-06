<img width="1512" height="982" alt="T_5" src="https://github.com/user-attachments/assets/9436adae-8c59-4c23-b900-1819bae870ee" /># Container Image Vulnerability Scanner with Reporting 

## Project Overview

This project is the Sprint 1 implementation of the **Container Image Vulnerability Scanner with Reporting** capstone project.

The objective is to scan Docker container images for known security vulnerabilities before deployment using **Trivy**.

The project uses the **ShopNow** application as the sample microservices application.

---

# Objective

Before deploying container images into production, they should be scanned for security vulnerabilities.

This project demonstrates how to:

- Build Docker images
- Scan images using Trivy
- Generate vulnerability reports
- Understand security risks in container images

---

# Project Architecture

```text
GitHub Repository
        │
        ▼
Clone Project
        │
        ▼
Build Docker Images
        │
        ▼
Run Docker Containers
        │
        ▼
Scan Images using Trivy
        │
        ▼
Generate JSON Reports
        │
        ▼
Review Vulnerabilities
```
---

# Technologies Used

| Tool | Purpose |
|------|---------|
| Docker | Build container images |
| Trivy | Vulnerability scanning |
| Git | Version Control |
| GitHub | Repository hosting |
| VS Code | Development |
| JSON | Scan reports |

---

# Project Structure

```text
shopNow/
│
├── backend/
│   └── Dockerfile
│
├── frontend/
│   └── Dockerfile
│
├── admin/
│   └── Dockerfile
│
├── reports/
│   ├── backend-report.json
│   ├── frontend-report.json
│   └── admin-report.json
│
├── docker-compose.yml
│
└── README.md
```
<img width="1684" height="1296" alt="image" src="https://github.com/user-attachments/assets/ee6602e4-9a75-448c-9939-54e8ce6b9192" />

---

# Installation

## Clone Repository

```bash
git clone https://github.com/mohanDevOps-arch/shopNow.git

cd shopNow
```
<img width="1670" height="510" alt="image" src="https://github.com/user-attachments/assets/022a6c86-1322-45be-bb03-c74565340f06" />

---

## Verify Docker

```bash
docker --version
```

Example

```text
Docker version 29.x.x
```
<img width="1682" height="736" alt="image" src="https://github.com/user-attachments/assets/eb0c9aa4-9eab-4ac0-9432-f07aefeee6ca" />

---

## Verify Trivy

```bash
trivy --version
```

Example

```text
Version: 0.xx.x
```
<img width="1682" height="566" alt="image" src="https://github.com/user-attachments/assets/70b53a29-1572-4c81-bc2c-eacd361d5668" />

---

# Build Docker Images

## Backend

```bash
cd backend

docker build -t shopnow-backend:v1 .
```
<img width="3020" height="900" alt="image" src="https://github.com/user-attachments/assets/d9908eed-1684-44f0-a800-e5f2a511c295" />

---

## Frontend

```bash
cd ../frontend

docker build -t shopnow-frontend:v1 .
```
<img width="3022" height="983" alt="image" src="https://github.com/user-attachments/assets/b505ce90-2ce6-4e25-9645-880277718a06" />

---

## Admin

```bash
cd ../admin

docker build -t shopnow-admin:v1 .
```
<img width="3022" height="981" alt="image" src="https://github.com/user-attachments/assets/315afc50-ed1c-4e06-8546-6f91483405d5" />

---

# Verify Images

```bash
docker images
```

Example

```text
shopnow-backend     v1
shopnow-frontend    v1
shopnow-admin       v1
```
<img width="3021" height="759" alt="image" src="https://github.com/user-attachments/assets/3b1e0027-65ae-45da-bd7d-73dff040accd" />

---

# Run Docker Containers

Backend

```bash
docker run -d \
--name backend-service |
--network shopnow-network \
-p 5001:5000 \
-e MONGODB_URI="mongodb://mongodb:27017/shopnow" \
shopnow-backend:v1
```
<img width="3024" height="594" alt="image" src="https://github.com/user-attachments/assets/56923ac5-a58d-43c3-a946-fb79a7e92c28" />
<img width="3016" height="338" alt="image" src="https://github.com/user-attachments/assets/1a653861-b1cb-49fb-ba25-2515d07d7e67" />

Frontend

```bash
docker run -d \
--name frontend \
--network shopnow-network \
-p 3000:80|
shopnow-frontend:v1
```
<img width="3024" height="200" alt="image" src="https://github.com/user-attachments/assets/2f3ece74-8e3c-448b-a9c5-69226914c8cf" />
<img width="3024" height="894" alt="image" src="https://github.com/user-attachments/assets/4cdd4f6f-c085-4f6f-bd1a-ab6bea0efa88" />

Admin

```bash
docker run -d |
--name admin \
--network shopnow-network \
-p 3001:80 |
shopnow-admin:v1
```
<img width="3024" height="1403" alt="image" src="https://github.com/user-attachments/assets/5f3bef21-1651-4b03-9278-0e40e5ebf09c" />
<img width="3022" height="867" alt="image" src="https://github.com/user-attachments/assets/18f59813-827b-40b1-be9f-d0987f57112b" />

---

# Scan Images Using Trivy

Backend

```bash
trivy image shopnow-backend:v1
```
<img width="1512" height="910" alt="T - 1" src="https://github.com/user-attachments/assets/a7af8f96-ea57-4256-82df-7cf172ec83d1" />
<img width="1511" height="903" alt="T - 2" src="https://github.com/user-attachments/assets/a4a039c7-fa22-4c62-8d94-1570e63e3e56" />
<img width="3023" height="1792" alt="image" src="https://github.com/user-attachments/assets/7e354032-abcb-4511-b918-78a1b5781189" />
<img width="3024" height="1819" alt="image" src="https://github.com/user-attachments/assets/1c5d255c-2087-4532-bc62-feb4297b3aea" />
<img width="3018" height="1773" alt="image" src="https://github.com/user-attachments/assets/dd350944-07d5-4821-a33e-82046ffc92d8" />
<img width="3020" height="1788" alt="image" src="https://github.com/user-attachments/assets/6dc3e01a-0236-49d0-aa33-9e94e66cfe7b" />
<img width="1512" height="907" alt="T - 7" src="https://github.com/user-attachments/assets/95c2299e-45c0-4b0c-a609-8b57a93a1f36" />
<img width="1512" height="531" alt="T - 8" src="https://github.com/user-attachments/assets/e6dc9be8-ea00-44fd-a8e0-07f909169bf3" />

Frontend

```bash
trivy image shopnow-frontend:v1
```
<img width="1512" height="346" alt="T-1" src="https://github.com/user-attachments/assets/088077fd-568e-4ee6-a632-f6320f67af1e" />
<img width="1510" height="728" alt="T-2" src="https://github.com/user-attachments/assets/4ec6b931-7524-4680-a60b-a217bc0fd541" />
<img width="1512" height="885" alt="T-3" src="https://github.com/user-attachments/assets/955d3659-9a42-4179-b27b-19346f096db9" />
<img width="1511" height="718" alt="T-4" src="https://github.com/user-attachments/assets/4fb5a2b0-1c41-4ead-812a-abadeb2d2597" />
<img width="1512" height="933" alt="T-5" src="https://github.com/user-attachments/assets/8f56d072-338f-4360-9b24-b1fe04f6ce0f" />

Admin

```bash
trivy image shopnow-admin:v1
```
<img width="1512" height="363" alt="T_1" src="https://github.com/user-attachments/assets/ccc8f106-b995-4ae2-803e-73372302d062" />
<img width="1511" height="729" alt="T_2" src="https://github.com/user-attachments/assets/513d6b52-d3ba-4069-80ab-e909609ad1d3" />
<img width="1512" height="871" alt="T_3" src="https://github.com/user-attachments/assets/a5ba6c5c-149d-4353-ae84-47ffdfa71009" />
<img width="1512" height="716" alt="T_4" src="https://github.com/user-attachments/assets/fe754915-c35f-46a2-a882-7254dd488141" />
<img width="1512" height="982" alt="T_5" src="https://github.com/user-attachments/assets/c95d5fe7-f55c-4352-baa3-880c65b8f238" />

---

# Generate JSON Reports

Create reports folder

```bash
mkdir reports
```
Backend Report

```bash
trivy image \
-f json \
-o reports/backend-report.json \
shopnow-backend:v1
```
<img width="3023" height="307" alt="image" src="https://github.com/user-attachments/assets/013fe0b1-fc31-4a4e-a30c-e0b6878f7dc8" />

Frontend Report

```bash
trivy image \
-f json \
-o reports/frontend-report.json \
shopnow-frontend:v1
```
<img width="3020" height="339" alt="image" src="https://github.com/user-attachments/assets/a2adac40-d328-4040-83c3-d7fcd413ab75" />

Admin Report

```bash
trivy image \
-f json \
-o reports/admin-report.json \
shopnow-admin:v1
```
<img width="3023" height="389" alt="image" src="https://github.com/user-attachments/assets/1626b6ce-ac64-4fdc-9f4b-eb1c7fd1edbb" />

---

# Sample Vulnerability Output

| Package | Installed | Fixed | Severity |
|----------|-----------|--------|----------|
| openssl | 3.0.2 | 3.0.15 | HIGH |
| busybox | 1.35 | 1.36 | MEDIUM |

---

# Reports Generated

```
reports/

backend-report.json

frontend-report.json

admin-report.json
```
<img width="1512" height="113" alt="R" src="https://github.com/user-attachments/assets/20acb9cf-065f-4f00-900d-227a7e1d18ee" />
<img width="3023" height="168" alt="image" src="https://github.com/user-attachments/assets/78e8cf8a-1174-471f-9c31-c15aa5aa82cf" />

---

# ✅ Sprint 1 Deliverables

- Clone ShopNow Repository
- Build Docker Images
- Run Docker Containers
- Scan Images using Trivy
- Generate JSON Reports
- Review Vulnerabilities

---

# 📸 Screenshots

git status 
git add.
git branch
git push
<img width="3023" height="784" alt="image" src="https://github.com/user-attachments/assets/e1c2c7f7-0474-4571-ab2d-b5994b1a380d" />

http://localhost:5001/api/health
<img width="1511" height="495" alt="Screenshot 2026-07-06 at 8 36 46 PM" src="https://github.com/user-attachments/assets/50118469-2baa-4579-833a-7999d415befa" />

http://localhost:3000
<img width="1510" height="641" alt="Screenshot 2026-07-06 at 9 45 09 PM" src="https://github.com/user-attachments/assets/c686fa0a-5d3f-4285-888e-01be92f555c8" />

http://localhost:3001
<img width="1511" height="758" alt="Screenshot 2026-07-06 at 9 44 57 PM" src="https://github.com/user-attachments/assets/01576b4d-dea9-40cd-8505-932eb623643c" />

Docker Dashborad (Images and Containers) 
<img width="1512" height="638" alt="Screenshot 2026-07-06 at 8 42 02 PM" src="https://github.com/user-attachments/assets/013e553b-9f74-4f9f-992f-01b97b6dd8d0" />
<img width="1510" height="947" alt="Screenshot 2026-07-06 at 8 41 56 PM" src="https://github.com/user-attachments/assets/7b95b19f-1a14-4f18-8488-94221dea0528" />

<img width="3023" height="1178" alt="image" src="https://github.com/user-attachments/assets/46289b67-199a-4f81-b520-883badfc55de" />
<img width="3024" height="1893" alt="image" src="https://github.com/user-attachments/assets/5c454f21-deb7-468c-bb05-1659d3e7cf3a" />

---

## Conclusion

Sprint 1 successfully demonstrates the implementation of a basic container image vulnerability scanning workflow using the ShopNow application. Docker images for the application's services were built, scanned with Trivy, and vulnerability reports were generated in JSON format for further analysis.

This project highlights the importance of integrating security checks early in the software development lifecycle by identifying known vulnerabilities before deployment. The generated reports provide valuable insights into the security posture of container images and establish a foundation for automated security validation.

In the next phase (Sprint 2), this manual process will be integrated into a CI/CD pipeline using tools such as GitHub Actions or Jenkins. The pipeline will automatically build Docker images, perform vulnerability scans, generate reports, and enforce security policies by failing builds when HIGH or CRITICAL vulnerabilities are detected, enabling a more secure and efficient DevSecOps workflow.

