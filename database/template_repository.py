from pathlib import Path
import sqlite3

DATABASE_PATH = Path(__file__).resolve().parent / "logs.db"
METRICS_DATABASE_PATH = Path(__file__).resolve().parent / "metrics.db"

class TemplateRepository:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def save_or_update(self, cluster_id, template, occurrences):

        existing = self.cursor.execute(
            "SELECT cluster_id FROM templates WHERE cluster_id=?",
            (cluster_id,)
        ).fetchone()

        if existing:

            self.cursor.execute(
                """
                UPDATE templates
                SET template=?,
                    occurrences=?,
                    last_seen=CURRENT_TIMESTAMP
                WHERE cluster_id=?
                """,
                (
                    template,
                    occurrences,
                    cluster_id
                )
            )

        else:

            self.cursor.execute(
                """
                INSERT INTO templates
                (
                    cluster_id,
                    template,
                    occurrences
                )
                VALUES (?, ?, ?)
                """,
                (
                    cluster_id,
                    template,
                    occurrences
                )
            )

        self.connection.commit()

    def get_all(self):

        self.cursor.execute(
            "SELECT * FROM templates"
        )

        return self.cursor.fetchall()

    def close(self):
        self.connection.close()