from pathlib import Path
import sqlite3
import sys

from database.template_repository import DATABASE_PATH





class LogRepository:
    
    def __init__(self):
        from pathlib import Path
       
        print("DB Path:", DATABASE_PATH)
        print("Exists:", DATABASE_PATH.exists())
        

        
        repository_connection = sqlite3.connect(DATABASE_PATH)
        self.connection = repository_connection
        self.cursor = self.connection.cursor()

    def save(self, event,cluster_id=None,template=None):
        repository=LogRepository

        try:
            if event.timestamp is None or event.level is None or event.message is None or event.uuid is None or event.logger_name is None or event.raw_log is None:
                raise ValueError("Event fields cannot be None")
            else:
                
                self.cursor.execute('''
            INSERT INTO logs (timestamp, level, message, uuid, logger_name, raw_log,cluster_id,template)
            VALUES (?, ?, ?, ?, ?, ?,?,?)
        ''', (event.timestamp, event.level, event.message, event.uuid, event.logger_name, event.raw_log,cluster_id,template))
                self.connection.commit()
        except Exception as e:
           raise Exception(e,sys)
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

