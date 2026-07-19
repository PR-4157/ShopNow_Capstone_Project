import subprocess
import shutil
import time
import sys

# Configuration
IMAGE = "shopnow-backend:v2"
OUTPUT = "reports/backend-report.json"
MAX_RETRIES = 3

# Check if Trivy is installed
if shutil.which("trivy") is None:
    print("❌ Trivy is not installed.")
    print("Install Trivy and try again.")
    sys.exit(1)


# Check if Docker is running
def check_docker():
    result = subprocess.run(
        ["docker", "info"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print("❌ Docker daemon is not running.")
        print("Start Docker Desktop and rerun the pipeline.")
        sys.exit(1)


print("Checking Docker...")
check_docker()

print("Checking Trivy...")
print("✅ Trivy is installed.\n")

# Retry scan
for attempt in range(1, MAX_RETRIES + 1):

    print(f"Attempt {attempt} of {MAX_RETRIES}")

    try:
        subprocess.run(
            [
                "trivy",
                "image",
                "-f", "json",
                "-o", OUTPUT,
                IMAGE
            ],
            check=True
        )

        print("✅ Scan completed successfully.")
        break

    except subprocess.CalledProcessError:
        print("❌ Trivy scan failed.")

        if attempt < MAX_RETRIES:
            print("Retrying in 5 seconds...\n")
            time.sleep(5)
        else:
            print(f"❌ Check that the Docker image '{IMAGE}' exists and try again.")
            sys.exit(1)