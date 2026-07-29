from pathlib import Path
import sqlite3

DATABASE_PATH = Path(__file__).resolve().parent / "metrics.db"


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Metrics(

 id INTEGER PRIMARY KEY AUTOINCREMENT,

timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

cpu_percent FLOAT,
memory_percent FLOAT,
disk_percent FLOAT,
network_sent INT,
network_recv INT,
process_count INT

)



""")