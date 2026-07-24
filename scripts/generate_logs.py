import logging
import os
import time
from datetime import datetime

from pathlib import Path

from numpy import random




LOG_DIR = Path("collector") / "sample_logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"
logging.basicConfig(
    filename=LOG_FILE,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

if __name__ == "__main__":

    messages = [
        "User Login",
        "Database Timeout",
        "Payment Success",
        "High CPU Usage",
        "Cache Miss",
        "File Uploaded",
    ]

    levels = [
        logging.info,
        logging.warning,
        logging.error,
    ]

    while True:
        random.choice(levels)(
            random.choice(messages)
        )

        time.sleep(2)