from pathlib import Path
import sqlite3


DATABASE_PATH = Path(__file__).resolve().parents[1] / "logs.db"





class LogRepository:
    
    def __init__(self):
        repository_connection = sqlite3.connect(DATABASE_PATH)
        self.connection = repository_connection
        self.cursor = self.connection.cursor()

    def save(self, event):
        try:
            if event.timestamp is None or event.level is None or event.message is None or event.uuid is None or event.logger_name is None or event.raw_log is None:
                raise ValueError("Event fields cannot be None")
            else:
                print(f"Saving event: {event}")
                self.cursor.execute('''
            INSERT INTO logs (timestamp, level, message, uuid, logger_name, raw_log)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (event.timestamp, event.level, event.message, event.uuid, event.logger_name, event.raw_log))
                self.connection.commit()
        except Exception as e:
           self.connection.rollback()

    def get_all(self):
        try:
            self.cursor.execute('SELECT * FROM logs')
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching logs: {e}")
            return []

    def get_all_logs(self):
        return self.get_all()

    def close(self):
        self.connection.close()
        return self.connection.close()