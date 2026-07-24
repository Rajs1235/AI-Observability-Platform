from pathlib import Path
from typing import Generator
import time


class LogReader:


    def __init__(self, log_file: str):
        self.log_file = Path(log_file)

        if not self.log_file.exists():
            raise FileNotFoundError(f"{self.log_file} does not exist.")

    def follow(self) -> Generator[str, None, None]:


        with self.log_file.open("r", encoding="utf-8") as file:

            # Skip existing logs.
            file.seek(0, 2)

            while True:

                line = file.readline()

                if not line:
                    time.sleep(0.2)
                    continue

                yield line.strip()