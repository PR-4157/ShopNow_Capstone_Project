#!/bin/bash

echo "=================================="
echo "Starting Trivy Image Scan"
echo "=================================="

# Create reports folder if it doesn't exist
mkdir -p reports

echo "Running Trivy Filesystem Scan..."
trivy fs -f json -o reports/trivy-fs.json .

echo "Scanning Backend Image..."
trivy image -f json -o reports/backend.json shopnow-backend:v1

echo "Scanning Frontend Image..."
trivy image -f json -o reports/frontend.json shopnow-frontend:v1

echo "Scanning Admin Image..."
trivy image -f json -o reports/admin.json shopnow-admin:v1

echo "Checking for HIGH and CRITICAL vulnerabilities..."
trivy image \
  --exit-code 1 \
  --severity HIGH,CRITICAL \
  shopnow-backend:v1

echo ""
echo "=================================="
echo "Scanning Completed!"
echo "Reports saved in reports/"
echo "=================================="