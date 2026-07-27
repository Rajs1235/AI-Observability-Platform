from pathlib import Path
import sys
import uuid
from datetime import datetime

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models.logevent import LogEvent
from database.repository import LogRepository

def main():
    repository = LogRepository()

    # Create a dummy LogEvent
    event = LogEvent(
        timestamp=datetime.now(),
        level="INFO",
        message="Repository Test Successful",
        uuid=str(uuid.uuid4()),
        logger_name="test_logger",
        raw_log="[2026-07-24 20:15:00] INFO Repository Test Successful"
    )

    # Save it
    repository.save(event)

    print(" Event saved successfully.\n")

    # Fetch all logs
    logs = repository.get_all_logs()

    print(f"Total Logs: {len(logs)}\n")

    for log in logs:
        print(log)


if __name__ == "__main__":
    main()