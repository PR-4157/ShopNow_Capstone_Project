# Container Image Vulnerability Scanner with Reporting

## Introduction

This project is a DevSecOps solution that scans Docker container images for security vulnerabilities using Trivy. It integrates with CI/CD pipelines to automate security scanning and generate vulnerability reports before deployment.

## Features

- Docker Image Vulnerability Scanning
- Trivy Integration
- GitHub Actions CI/CD
- Jenkins Pipeline Support
- JSON & HTML Reports
- Historical Scan Comparison
- Exception Handling
- Retry Logic

## Architecture

Developer
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Actions
      │
      ▼
Docker Build
      │
      ▼
Trivy Scan
      │
      ▼
Security Reports

## Requirements

- Docker Desktop
- Trivy
- Python 3.x
- Git
- GitHub Account

## Installation

### Clone Repository

git clone https://github.com/yourusername/ShopNow_Capstone_Project.git

### Move into Project

cd ShopNow_Capstone_Project

### Install Docker

Install Docker Desktop from Docker's official website.

### Install Trivy

Follow the Trivy installation guide for your operating system.

### Build Images

./scripts/build.sh


## Configuration

Update image names in scripts/scan.sh.

Modify severity levels:

HIGH
CRITICAL

Change output folder if required.

## Usage

Build Docker images

./scripts/build.sh

Run Trivy Scan

./scripts/scan.sh

View Reports

reports/

## Deployment

Run the deployment script to prepare the environment:

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

The script will:

- Verify Docker installation
- Verify Trivy installation
- Create required folders
- Make project scripts executable
- Build Docker images


## CI/CD Integration

The scanner integrates with:

- GitHub Actions
- Jenkins

Every push automatically triggers security scanning.

## Dashboard

Grafana displays:

- Vulnerability Trends
- Scan History
- Severity Distribution

## Troubleshooting

Docker daemon not running

Start Docker Desktop.

Trivy not installed

Install Trivy.

Docker image not found

Run build.sh before scan.sh.

## Folder Structure

ShopNow_Capstone_Project
│
├── .github
│   └── GitHub Actions workflows
│
├── config
│   └── Configuration files
│
├── reports
│   ├── JSON Reports
│   ├── HTML Reports
│   └── history
│
├── scripts
│   ├── build.sh
│   ├── scan.sh
│   ├── compare_reports.py
│   ├── retry_scan.py
│   └── exception_handler.py
│
├── shopNow
│   └── Application source code
│
├── Jenkinsfile
│
└── README.md

## Future Improvements

- Kubernetes Integration
- Multi-image parallel scanning
- Email notifications
- Additional vulnerability scanners
- Cloud deployment

