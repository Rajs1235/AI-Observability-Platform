import psutil
import re
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
from models.metrics_event import MetricsEvent
from database.repository import MetricsRepository




def collect_metrics() -> MetricsEvent | None:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    network = psutil.net_io_counters()

    processes = len(psutil.pids())
    print(f"CPU:{cpu},MEMORY:{memory},DISK:{disk},NETWORK:{network},PROCESSES:{processes}")

    return MetricsEvent(
        timestamp=datetime.now().isoformat(),
        cpu_percent=cpu,
        memory_percent=memory,
        disk_percent=disk,
        network_sent=network.bytes_sent,
        network_recv=network.bytes_recv,
        process_count=processes,
    )


def main():
    repository = MetricsRepository()
    
    try:
        while True:
            event = collect_metrics()
            repository.save(event)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        repository.close()


if __name__ == "__main__":
    main()