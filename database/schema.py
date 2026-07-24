import sqlite3

connection = sqlite3.connect('logs.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    level TEXT NOT NULL,
    message TEXT NOT NULL,
    uuid TEXT NOT NULL,
    logger_name TEXT NOT NULL,
    raw_log TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''CREATE Index IF NOT EXISTS idx_logs_timestamp ON logs (timestamp)''')

connection.commit()
connection.close()