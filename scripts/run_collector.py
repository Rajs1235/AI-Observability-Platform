import re
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path

# Add project root to Python path (this file lives in scripts/, so root is one level up)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models.log_event import LogEvent
from database.repository import LogRepository

LOG_FILE = PROJECT_ROOT / "collector" / "sample_logs" / "app.log"

# Tracks how many bytes of app.log we've already read, so restarting this
# script doesn't re-insert lines that were already saved to the DB.
STATE_FILE = PROJECT_ROOT / "collector" / "sample_logs" / ".collector_offset"

# Matches: [2026-07-26 05:05:14,323] 42 app_logger - INFO - User Login
LOG_LINE_RE = re.compile(
    r"^\[(?P<timestamp>[^\]]+)\]\s+(?P<lineno>\d+)\s+(?P<logger_name>\S+)\s+-\s+"
    r"(?P<level>\w+)\s+-\s+(?P<message>.*)$"
)


def read_offset() -> int:
    if STATE_FILE.exists():
        try:
            return int(STATE_FILE.read_text().strip())
        except ValueError:
            return 0
    return 0


def write_offset(offset: int) -> None:
    STATE_FILE.write_text(str(offset))


def parse_line(raw_line: str) -> LogEvent | None:
    match = LOG_LINE_RE.match(raw_line.strip())
    if not match:
        return None

    data = match.groupdict()
    try:
        timestamp = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S,%f")
    except ValueError:
        timestamp = datetime.now()

    return LogEvent(
        timestamp=timestamp,
        level=data["level"].upper(),
        message=data["message"],
        uuid=str(uuid.uuid4()),
        logger_name=data["logger_name"],
        raw_log=raw_line.strip(),
    )


def collect_once(repository: LogRepository) -> int:
    """Read any new lines appended to LOG_FILE since the last run and save them."""
    if not LOG_FILE.exists():
        return 0

    offset = read_offset()
    saved = 0

    with open(LOG_FILE, "r") as f:
        f.seek(offset)
        for line in f:
            if not line.strip():
                continue
            event = parse_line(line)
            if event is None:
                print(f"Skipping unparseable line: {line.strip()}")
                continue
            repository.save(event)
            saved += 1
        new_offset = f.tell()

    write_offset(new_offset)
    return saved


def main():
    repository = LogRepository()
    print(f"Watching {LOG_FILE} for new log lines. Ctrl+C to stop.")
    try:
        while True:
            saved = collect_once(repository)
            if saved:
                print(f"Saved {saved} new log entr{'y' if saved == 1 else 'ies'} to the database.")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        repository.close()


if __name__ == "__main__":
    main()