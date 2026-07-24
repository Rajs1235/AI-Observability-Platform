from dataclasses import dataclass


@dataclass
class LogEvent:
    timestamp: str
    level: str
    message: str
    uuid: str
    logger_name: str
    raw_log: str
