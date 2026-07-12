#!/bin/bash

# Load environment variables
source .env

echo "=================================="
echo "Starting Security Scan"
echo "=================================="

# Create reports directory
mkdir -p "$REPORTS_DIR"

################################################
# GitLeaks Scan
################################################

echo ""
echo "Running GitLeaks Scan..."

gitleaks detect \
  --source . \
  --report-format json \
  --report-path "$REPORTS_DIR/gitleaks-report.json"

################################################
# Trivy Filesystem Scan
################################################

echo ""
echo "Running Trivy Filesystem Scan..."

trivy fs \
  -f "$TRIVY_FORMAT" \
  -o "$REPORTS_DIR/trivy-fs.json" \
  .

################################################
# Backend Image Scan
################################################

echo ""
echo "Scanning Backend Image..."

trivy image \
  -f "$TRIVY_FORMAT" \
  -o "$REPORTS_DIR/backend-report.json" \
  "$BACKEND_IMAGE"

################################################
# Frontend Image Scan
################################################

echo ""
echo "Scanning Frontend Image..."

trivy image \
  -f "$TRIVY_FORMAT" \
  -o "$REPORTS_DIR/frontend-report.json" \
  "$FRONTEND_IMAGE"

################################################
# Admin Image Scan
################################################

echo ""
echo "Scanning Admin Image..."

trivy image \
  -f "$TRIVY_FORMAT" \
  -o "$REPORTS_DIR/admin-report.json" \
  "$ADMIN_IMAGE"

################################################
# Security Gate
################################################

echo ""
echo "Checking for HIGH and CRITICAL vulnerabilities..."

trivy image \
  --exit-code 1 \
  --severity "$SEVERITY" \
  "$BACKEND_IMAGE"

echo ""
echo "=================================="
echo "Scanning Completed!"
echo "Reports saved in $REPORTS_DIR"
echo "=================================="