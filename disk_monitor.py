import shutil
import string
from datetime import datetime
import os

# Log file path
log_file = "disk_report.log"

# Function to log message to console and file
def log(message):
    print(message)
    with open(log_file, "a") as f:
        f.write(message + "\n")

log("=== Disk Usage Check ===")
log(f"Timestamp: {datetime.now()}")
log("----------------------")

# Loop through all possible drives
for letter in string.ascii_uppercase:
    drive = f"{letter}:\\"
    if not os.path.exists(drive):
        continue  # Skip non-existing drives

    total, used, free = shutil.disk_usage(drive)

    # Convert bytes to GB
    total_gb = total // (2**30)
    used_gb = used // (2**30)
    free_gb = free // (2**30)

    log(f"Drive: {drive}")
    log(f"Total: {total_gb} GB")
    log(f"Used : {used_gb} GB")
    log(f"Free : {free_gb} GB")

    # Status logic
    if free_gb < 10:
        status = "CRITICAL"
    elif free_gb < 20:
        status = "WARNING"
    else:
        status = "HEALTHY"

    log(f"Status: {status}")
    log("----------------------")