from analyx.settings import PLUGINS
from tortoise import Tortoise, run_async
from typing import List

DB_URL = "sqlite://db.sqlite3"

async def initdb(plugin_models: List, **kwargs):
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"

    await Tortoise.init(
        db_url=self.db, modules={"models": plugin_models}
    )  # ['app.models']}
    # Generate the schema
    await Tortoise.generate_schemas()

# run_async is a helper function to run simple async Tortoise scripts.
def asyncdb(**kwargs):
    run_async(initdb(**kwargs))

def addPlugin(loc: str):
    pass
class StorageHandler:
    def __init__(self, plugins: List = PLUGINS, loc: str = DB_URL):
        self.plugins: List = plugins
        self.db: str = loc
        self.plugin_models: List[str] = [f"{x}.models" for x in self.plugins]
        for plg in self.plugins:
            globals()[f"{plg}.models"] = __import__(f"{plg}.models")


if __name__ == "__main__":
    print("Hi!")