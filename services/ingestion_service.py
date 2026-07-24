from database.repository import LogRepository
from parser.parser import LogParser


class IngestionService:
    def __init__(self):
        self.parser = LogParser()
        self.repository = LogRepository()
        self._line_number = 0

    def process(self, raw_log: str):
        self._line_number += 1
        event = self.parser.parse(raw_log, self._line_number)

        if event is None:
            return None

        self.repository.save(event)
        return event

    def close(self):
        self.repository.close()
