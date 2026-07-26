#!/bin/bash

echo "====================================="
echo " ShopNow Security Scanner Setup"
echo "====================================="

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed."
    exit 1
fi

echo "Docker found."

# Check Trivy
if ! command -v trivy &> /dev/null; then
    echo "Trivy is not installed."
    exit 1
fi

echo "Trivy found."

# Create required directories
echo "Creating required folders..."

mkdir -p reports
mkdir -p reports/history
mkdir -p logs

echo "Folders created."

# Make scripts executable
chmod +x scripts/build.sh
chmod +x scripts/scan.sh

echo "Scripts are executable."

# Build Docker images
echo "Building Docker images..."
./scripts/build.sh

echo "====================================="
echo "Environment setup completed."
echo "Run the scan using:"
echo "./scripts/scan.sh"
echo "====================================="