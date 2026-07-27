import sqlite3

conn = sqlite3.connect("database/logs.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM logs")
print("Total Logs:", cursor.fetchone()[0])

cursor.execute("SELECT id, level, message FROM logs ORDER BY id DESC LIMIT 10")
for row in cursor.fetchall():
    print(row)

conn.close()