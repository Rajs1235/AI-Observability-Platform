from dataclasses import dataclass

import datetime

@dataclass
class MetricsEvent:
    timestamp:datetime
    cpu_percent:float
    memory_percent:float
    disk_percent:float
    network_sent:int
    network_recv:int
    process_count:int