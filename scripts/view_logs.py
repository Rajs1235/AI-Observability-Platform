from pathlib import Path
import sys

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.repository import LogRepository


def main():
    repository = LogRepository()

    try:
        logs = repository.get_all()

        if not logs:
            print("No logs found in the database.")
            return

        print(f"\nFound {len(logs)} log(s).\n")

        for log in logs:
            print("=" * 80)
            print(f"ID         : {log[0]}")
            print(f"Timestamp  : {log[1]}")
            print(f"Level      : {log[2]}")
            print(f"Message    : {log[3]}")
            print(f"UUID       : {log[4]}")
            print(f"Logger     : {log[5]}")
            print(f"Raw Log    : {log[6]}")
            print(f"Created At : {log[7]}")
            print("=" * 80)

    finally:
        repository.close()


if __name__ == "__main__":
    main()