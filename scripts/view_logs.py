from pathlib import Path
import sys
from fastapi import FastAPI
# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.repository import LogRepository

app=FastAPI()

@app.get("/logs")
async def get_logs():
    repository = LogRepository()
    
    try:
        logs = repository.get_all()
    
        if not logs:
                    return {"message": "No logs found in the database."}
    
        return [
                    {
                         "ID": log[0],
                         "Timestamp": log[1],
                         "Level": log[2],
                         "Message": log[3],
                         "UUID": log[4],
                         "Logger": log[5],
                         "Raw Log": log[6],
                         "Created At": log[7],
                    }
                    for log in logs
               ]
    
    finally:
            repository.close()
@app.get("/logs/search")
async def search_log(query):
        repository=LogRepository()
        p=str(query)
        try:
            pattern = f"%{query}%"

            logs = repository.cursor.execute(
    "SELECT * FROM logs WHERE message LIKE ?",
    (pattern,)
).fetchall()
            if not logs:
                 return {"message":"No logs found"}
            return logs
        except Exception as e:
            return {"error":str(e)}
        finally:
            repository.close()   
@app.get("/logs/{log_id}")
async def get_log_by_id(log_id: int):
    repository=LogRepository()
    try:
        log=repository.cursor.execute("SELECT * FROM logs where id=?", (log_id,)).fetchone()
        if log is None:
                return {"message": f"No log found with ID {log_id}"}
        return {
            "ID": log[0],
            "Timestamp": log[1],
            "Level": log[2],
            "Message": log[3],
            "UUID": log[4],
            "Logger": log[5],
            "Raw Log": log[6],
            "Created At": log[7]
        }
    except Exception as e:
            return {"error": str(e)}

@app.get("/recentlogs")
async def get_recent_logs():
     repository=LogRepository()
     try:
        logs = repository.cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 6").fetchall()
        if not logs:
            return {"message":f"No logs found"}
        return [
             {
                  "ID": log[0],
                  "Timestamp": log[1],
                  "Level": log[2],
                  "Message": log[3],
                  "UUID": log[4],
                  "Logger": log[5],
                  "Raw Log": log[6],
                  "Created At": log[7]
             }
             for log in logs
        ]
     except Exception as e:
          return {"error":str(e)}
     finally:
          repository.close()

@app.get("/error")
async def get_errors():
     repository=LogRepository()
     try:
          logs=repository.cursor.execute("SELECT * FROM logs WHERE level='ERROR'").fetchall()
          if not logs:
               return {"message":f"No logs found"}
          return [
               {
                    "ID": log[0],
                    "Timestamp": log[1],
                    "Level": log[2],
                    "Message": log[3],
                    "UUID": log[4],
                    "Logger": log[5],
                    "Raw Log": log[6],
                    "Created At": log[7]
               }
               for log in logs
          ]
     except Exception as e:
          return {"error":str(e)}
     finally:
          repository.close()
           
@app.get("/warning")
async def get_all_warnings():
     repository=LogRepository()
     try:
          logs=repository.cursor.execute("SELECT * FROM logs WHERE level='WARNING'").fetchall()
          if not logs:
               return {"message":f"No logs found"}
          return [
               {
                    "ID": log[0],
                    "Timestamp": log[1],
                    "Level": log[2],
                    "Message": log[3],
                    "UUID": log[4],
                    "Logger": log[5],
                    "Raw Log": log[6],
                    "Created At": log[7]
               }
               for log in logs
          ]
     except Exception as e:
          return {"error":str(e)}
     finally:
          repository.close()

@app.get("/top10error")
async def get_top_10_errors():
     repository=LogRepository()
     try:
          logs=repository.cursor.execute("SELECT message, count(*) FROM logs WHERE level='ERROR' GROUP BY message ORDER BY count(message) DESC LIMIT 10").fetchall()
          if not logs:
               return {"message":f"No logs found"}
          return [
                                        {
                                             "Message": log[0],
                                             "Count": log[1]
                                        }
                                        for log in logs
                                   ]
          
     except Exception as e:
          return {"error":str(e)}
     finally:
          repository.close()

@app.get("/top10logger")
async def get_top_10_loggers():
     repository=LogRepository()
     try:
          logs=repository.cursor.execute("SELECT logger_name, count(*) FROM logs WHERE level='INFO' GROUP BY logger_name ORDER BY count(*) DESC LIMIT 10").fetchall()
          if not logs:
               return {"message":"No logs found"}
               

          return [
                                                       {
                                                            "Message": log[0],
                                                            "Count": log[1]
                                                       }
                                                       for log in logs
                                                  ]
          
     except Exception as e:
          return {"error":str(e)}
     finally:
          repository.close()


@app.get("/stats")
async def get_stats():
    repository = LogRepository()

    try:
        total_logs = repository.cursor.execute("""
            SELECT COUNT(*)
            FROM logs
        """).fetchone()[0]

        error_logs = repository.cursor.execute("""
            SELECT COUNT(*)
            FROM logs
            WHERE level='ERROR'
        """).fetchone()[0]

        warning_logs = repository.cursor.execute("""
            SELECT COUNT(*)
            FROM logs
            WHERE level='WARNING'
        """).fetchone()[0]

        info_logs = repository.cursor.execute("""
            SELECT COUNT(*)
            FROM logs
            WHERE level='INFO'
        """).fetchone()[0]

        unique_loggers = repository.cursor.execute("""
            SELECT COUNT(DISTINCT logger_name)
            FROM logs
        """).fetchone()[0]

        top_loggers = repository.cursor.execute("""
            SELECT logger_name, COUNT(*) AS count
            FROM logs
            GROUP BY logger_name
            ORDER BY count DESC
            LIMIT 10
        """).fetchall()
        total_templates = repository.cursor.execute("""
SELECT COUNT(*)
FROM templates
""").fetchone()[0]

        total_template_occurrences = repository.cursor.execute("""
SELECT SUM(occurrences)
FROM templates
""").fetchone()[0]

        return {
            "total_logs": total_logs,
            "error_logs": error_logs,
            "warning_logs": warning_logs,
            "info_logs": info_logs,
            "total_templates":total_templates,
            "total_template_occurrences":total_template_occurrences,
            "unique_loggers": unique_loggers,
            "top_loggers": [
                {
                    "logger_name": logger,
                    "count": count
                }
                for logger, count in top_loggers
            ]
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        repository.close()
@app.get("/templates")
async def get_template_summary():
    repository = LogRepository()

    try:
        total_templates = repository.cursor.execute("""
            SELECT COUNT(*)
            FROM templates
        """).fetchone()[0]

        total_occurrences = repository.cursor.execute("""
            SELECT SUM(occurrences)
            FROM templates
        """).fetchone()[0]

        return {
            "total_templates": total_templates,
            "total_occurrences": total_occurrences
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        repository.close()

@app.get("/templates/all")
async def get_all_templates():
    repository = LogRepository()

    try:
        templates = repository.cursor.execute("""
            SELECT cluster_id,
                   template,
                   occurrences,
                   first_seen,
                   last_seen
            FROM templates
            ORDER BY cluster_id
        """).fetchall()

        return [
            {
                "cluster_id": row[0],
                "template": row[1],
                "occurrences": row[2],
                "first_seen": row[3],
                "last_seen": row[4]
            }
            for row in templates
        ]

    except Exception as e:
        return {"error": str(e)}

    finally:
        repository.close()

@app.get("/templates/top")
async def get_top_templates():
    repository = LogRepository()

    try:
        templates = repository.cursor.execute("""
            SELECT cluster_id,
                   template,
                   occurrences
            FROM templates
            ORDER BY occurrences DESC
            LIMIT 10
        """).fetchall()

        return [
            {
                "cluster_id": row[0],
                "template": row[1],
                "occurrences": row[2]
            }
            for row in templates
        ]

    except Exception as e:
        return {"error": str(e)}

    finally:
        repository.close()

@app.get("/templates/recent")
async def get_recent_templates():
    repository = LogRepository()

    try:
        templates = repository.cursor.execute("""
            SELECT cluster_id,
                   template,
                   last_seen
            FROM templates
            ORDER BY last_seen DESC
            LIMIT 10
        """).fetchall()

        return [
            {
                "cluster_id": row[0],
                "template": row[1],
                "last_seen": row[2]
            }
            for row in templates
        ]

    except Exception as e:
        return {"error": str(e)}

    finally:
        repository.close()

@app.get("/templates/rare")
async def get_rare_templates():
    repository = LogRepository()

    try:
        templates = repository.cursor.execute("""
            SELECT cluster_id,
                   template,
                   occurrences
            FROM templates
            ORDER BY occurrences ASC
            LIMIT 10
        """).fetchall()

        return [
            {
                "cluster_id": row[0],
                "template": row[1],
                "occurrences": row[2]
            }
            for row in templates
        ]

    except Exception as e:
        return {"error": str(e)}

    finally:
        repository.close()

@app.get("/templates/{cluster_id}")
async def get_templatebyid(cluster_id: int):
    repository = LogRepository()

    try:
        template = repository.cursor.execute("""
            SELECT cluster_id,
                   template,
                   occurrences,
                   first_seen,
                   last_seen
            FROM templates
            WHERE cluster_id=?
        """, (cluster_id,)).fetchone()

        if template is None:
            return {"error": "Template not found"}

        return {
            "cluster_id": template[0],
            "template": template[1],
            "occurrences": template[2],
            "first_seen": template[3],
            "last_seen": template[4]
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        repository.close()