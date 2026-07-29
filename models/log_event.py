from dataclasses import dataclass

import datetime
@dataclass
class LogEvent:
    timestamp: datetime
    level: str
    message: str
    uuid:str
    logger_name: str
    raw_log:str