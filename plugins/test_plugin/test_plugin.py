from analyx.plugins import Plugin
from analyx.database import DB_URL
from pathlib import Path

class HitCounter(Plugin):
    def __init__(self, db):
        self.db: str = db

    def output(self):
        print("Hello! This is a test plugin!")


if __name__ == "__main__":
    a = HitCounter(DB_URL)
    a.output()
    print(dir(a))
    print(str(Path(__file__).resolve().parent.parent))
