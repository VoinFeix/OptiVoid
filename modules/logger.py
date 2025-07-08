# modules/logger.py

import os
from datetime import datetime

LOG_FILE = os.path.expanduser("~/optivoid_logs.txt")

def write_log(message):
    time_stamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_message = f"{time_stamp} {message}\n"

    try:
        with open(LOG_FILE, "a") as f:
            f.write(log_message)

    except Exception as e:
        print(f"[!] Failed to write to log: {e}")