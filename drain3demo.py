from drain3.template_miner import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
from drain3_engine.engine import Drain3Engine
# Load default configuration
config = TemplateMinerConfig()
from pathlib import Path
from database.repository import LogRepository
from database.template_repository import TemplateRepository
config.load(str(Path(__file__).parent / "drain3.ini")) # We'll create this file next

# Initialize TemplateMiner
template_miner = TemplateMiner(config=config)

engine = Drain3Engine()

log_repository = LogRepository()

template_repository = TemplateRepository()

logs = log_repository.get_all()

engine.process_logs([log[3] for log in logs])

engine.update_repository(template_repository)

print(template_repository.get_all())