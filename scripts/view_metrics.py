from pathlib import Path
import sys
from fastapi import FastAPI
# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.repository import MetricsRepository

app=FastAPI()

@app.get("/metrics")
def getmetrics():
    repository=MetricsRepository()
    try:
        metric=repository.get_all()
        if not metric:
            return {"message":"No metric found"}
        return [
            { "ID": metric[0],
                                     "Timestamp": metric[1],
                                     "cpu_percent": metric[2],
                                     "memory_percent": metric[3],
                                     "disk_percent": metric[4],
                                     "network_sent": metric[5],
                                     "network_recv": metric[6],
                                     "process_count": metric[7],}
            for met in metric
        ]

    except Exception as e:
      return {"error":e}

app.get("/metrics/latest")
def getlatestmetric():
    repository=MetricsRepository()
    try:
        pass
    except Exception as e:
        return {"error":e}