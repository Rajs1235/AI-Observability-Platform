import sys
import time
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from services.ingestion_service import IngestionService

LOG_FILE = PROJECT_ROOT / "collector" / "sample_logs" / "app.log"

STATE_FILE = PROJECT_ROOT / "collector" / "sample_logs" / ".collector_offset"

print("Reading logs from:", LOG_FILE)
def read_offset() -> int:
    if STATE_FILE.exists():
        try:
            return int(STATE_FILE.read_text().strip())
        except ValueError:
            return 0
    return 0


def write_offset(offset: int) -> None:
    STATE_FILE.write_text(str(offset))


def collect_once(service: IngestionService) -> int:
    """
    Read any new log lines appended to LOG_FILE since the previous run
    and process them through the ingestion pipeline.
    """

    if not LOG_FILE.exists():
        return 0

    offset = read_offset()
    processed = 0

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        f.seek(offset)

        for line in f:
            line = line.strip()
            print("READ:", line.strip())

            if not line:
                continue

            event = service.process(line)

            if event is not None:
                processed += 1

        new_offset = f.tell()

    write_offset(new_offset)

    return processed


def main():
    service = IngestionService()

    print(f"Watching {LOG_FILE} for new log lines. Press Ctrl+C to stop.")

    try:
        while True:
            processed = collect_once(service)

            if processed:
                print(f"Processed {processed} new log entr{'y' if processed == 1 else 'ies'}.")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopped.")

    finally:
        service.close()


if __name__ == "__main__":
    main()