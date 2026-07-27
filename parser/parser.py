from dataclasses import dataclass
from datetime import datetime
import uuid
from models.log_event import LogEvent

class LogParser:

    def parse(self, log_line: str, line_number: int) -> LogEvent:
        try:
            # Split the log line into its components
            timestamp_str, rest = log_line.split("] ", 1)
            timestamp_str = timestamp_str.strip("[")
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S,%f")

            # Further split the rest of the log line
            parts = rest.split(" - ")
            if len(parts) < 3:
                raise ValueError("Log line does not have enough parts")

            logger_name = parts[0].strip()
            level = parts[1].strip()
            message = " - ".join(parts[2:]).strip()
            uuid_str=str(uuid.uuid4())

            return LogEvent(
                timestamp=timestamp.isoformat(),
                level=level,
                uuid=uuid_str,
                message=message,
                line_number=line_number,
                logger_name=logger_name,
                raw_log=log_line
            )
        except Exception as e:
            print(f"Error parsing log line {line_number}: {e}")
            return None