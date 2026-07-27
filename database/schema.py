from pathlib import Path
import sqlite3

DATABASE_PATH = Path(__file__).resolve().parent / "logs.db"

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

    level TEXT NOT NULL,

    message TEXT NOT NULL,

    uuid TEXT NOT NULL,

    logger_name TEXT NOT NULL,

    raw_log TEXT NOT NULL,

    cluster_id INTEGER,

    template TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(cluster_id)
    REFERENCES templates(cluster_id)
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS templates(

    cluster_id INTEGER PRIMARY KEY,

    template TEXT NOT NULL,

    occurrences INTEGER DEFAULT 0,
    level TEXT,

    first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,

    last_seen DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

 
cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_logs_timestamp
ON logs(timestamp)
""")
cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_logs_level
ON logs(level);
""")
cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_logs_cluster
ON logs(cluster_id);
""")
connection.commit()
connection.close()