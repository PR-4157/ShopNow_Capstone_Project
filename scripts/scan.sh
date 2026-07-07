#!/bin/bash

# Load environment variables
source .env

echo "=================================="
echo "Starting Trivy Image Scan"
echo "=================================="

# Create reports folder if it doesn't exist
mkdir -p reports

echo ""
echo "Running Trivy Filesystem Scan..."
trivy fs \
  -f "$TRIVY_FORMAT" \
  -o "$REPORTS_DIR/trivy-fs.json" \
  .

echo ""
echo "Scanning Backend Image..."
trivy image \
  -f "$TRIVY_FORMAT" \
  -o "$REPORTS_DIR/backend-report.json" \
  "$BACKEND_IMAGE"

echo ""
echo "Scanning Frontend Image..."
trivy image \
  -f "$TRIVY_FORMAT" \
  -o "$REPORTS_DIR/backend-report.json" \
  "$FRONTEND_IMAGE"

echo ""
echo "Scanning Admin Image..."
trivy image \
  -f "$TRIVY_FORMAT" \
  -o "$REPORTS_DIR/backend-report.json" \
  "$ADMIN_IMAGE"

echo ""
echo "Checking for HIGH and CRITICAL vulnerabilities..."
trivy image \
  --exit-code 1 \
  --severity "$SEVERITY" \
  "$BACKEND_IMAGE"

echo ""
echo "=================================="
echo "Scanning Completed!"
echo "Reports saved in reports/"
echo "=================================="