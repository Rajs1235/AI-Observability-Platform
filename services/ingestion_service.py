from database.repository import LogRepository
from parser.parser import LogParser
from drain3_engine.engine import Drain3Engine
from database.template_repository import TemplateRepository

class IngestionService:
  
    def __init__(self):
        self.parser = LogParser()
        self.repository = LogRepository()
        self.template_repository=TemplateRepository()
      
        self.drain3=Drain3Engine()
        self._line_number = 0

    def process(self, raw_log: str):
        self._line_number += 1
        event = self.parser.parse(raw_log, self._line_number)
        

        if event is None:
            return None

        cluster_id,template,cluster_size=self.drain3.process_log(event.message)

        self.repository.save(event,cluster_id,template)
        self.template_repository.save_or_update(
    cluster_id,template,cluster_size
     )

        return event

    def close(self):
        self.repository.close()
