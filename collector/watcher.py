from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Allow both `python collector/watcher.py` and
# `python -m collector.watcher`
if __package__ in {None, ""} and str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from collector.reader import LogReader
from services.ingestion_service import IngestionService
LOG_FILE = Path(__file__).resolve().parent / "sample_logs" / "app.log"


def main():
    if not LOG_FILE.exists():
        print(f"Log file not found: {LOG_FILE}")
        return

    reader = LogReader(LOG_FILE)
    service = IngestionService()

    print(f"Watching: {LOG_FILE.resolve()}")
    print(f"Exists: {LOG_FILE.exists()}")
    print(f"Size: {LOG_FILE.stat().st_size} bytes\n")

    try:
        for log in reader.follow():
            event = service.process(log)

            if event is not None:
                print(event)

    except KeyboardInterrupt:
        print("\nStopped watching.")
    finally:
        service.close()


if __name__ == "__main__":
    main()