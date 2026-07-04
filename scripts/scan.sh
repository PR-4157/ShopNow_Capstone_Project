#!/bin/bash

echo "=================================="
echo "Starting Trivy Image Scan"
echo "=================================="

# Create reports folder if it doesn't exist
mkdir -p reports

echo ""
echo "Scanning Backend Image..."
trivy image -f json -o reports/backend.json shopnow-backend:v1

echo ""
echo "Scanning Frontend Image..."
trivy image -f json -o reports/frontend.json shopnow-frontend:v1

echo ""
echo "Scanning Admin Image..."
trivy image -f json -o reports/admin.json shopnow-admin:v1

echo ""
echo "=================================="
echo "Scanning Completed!"
echo "Reports saved in reports/"
echo "=================================="