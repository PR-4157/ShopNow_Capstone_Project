import subprocess
from datetime import datetime
from pathlib import Path

# Create the history folder if it doesn't exist
history_dir = Path("reports/history")
history_dir.mkdir(parents=True, exist_ok=True)

# Docker image to scan
image = "shopnow-backend:v1"

# Current date and time
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Output file
output_file = history_dir / f"backend-{timestamp}.json"

print(f"Scanning {image}...")
print(f"Saving report to {output_file}")

subprocess.run([
    "trivy",
    "image",
    "-f", "json",
    "-o", str(output_file),
    image
], check=True)

print("Scan completed.")