from pathlib import Path
import logging
import time
from numpy import random

PROJECT_ROOT = Path(__file__).resolve().parents[1]

LOG_DIR = PROJECT_ROOT / "collector" / "sample_logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

print("Writing logs to:", LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

# Every lambda generates a NEW log message
messages = [
    lambda: f"User {random.randint(1000,9999)} logged in",
    lambda: f"User {random.randint(1000,9999)} logged out",

    lambda: f"Payment for Order {random.randint(10000,99999)} completed",
    lambda: f"Payment for Order {random.randint(10000,99999)} failed",

    lambda: f"Database timeout after {random.randint(10,60)} seconds",

    lambda: f"CPU usage reached {random.randint(70,100)}%",
    lambda: f"Memory usage reached {random.randint(60,100)}%",
    lambda: f"Disk usage reached {random.randint(70,100)}%",

    lambda: f"Cache miss for key USER_{random.randint(100,999)}",

    lambda: f"File report_{random.randint(1,500)}.pdf uploaded",

    lambda: f"Request GET /api/orders took {random.randint(20,800)} ms",
    lambda: f"Request POST /api/payment took {random.randint(50,1500)} ms",

    lambda: f"Connection from 192.168.1.{random.randint(1,254)} accepted",

    lambda: f"Worker {random.randint(1,5)} restarted",

    lambda: f"Service auth restarted after {random.randint(1,5)} crashes",
]

levels = [
    logging.info,
    logging.warning,
    logging.error,
]

if __name__ == "__main__":
    while True:
        level = random.choice(levels)
        message = random.choice(messages)()

        level(message)

        time.sleep(2)