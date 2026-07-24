from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogEvent:
    timestamp: datetime
    level: str
    message: str
    line_number: int
    logger_name: str

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

            return LogEvent(
                timestamp=timestamp,
                level=level,
                message=message,
                line_number=line_number,
                logger_name=logger_name
            )
        except Exception as e:
            print(f"Error parsing log line {line_number}: {e}")
            return None