from dataclasses import dataclass

import datetime
@dataclass
class LogEvent:
    timestamp: datetime
    level: str
    message: str
    uuid:str
    line_number: int
    logger_name: str
    raw_log:str