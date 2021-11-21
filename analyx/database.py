from .settings import PLUGINS
from tortoise import Tortoise, run_async

DB_URL = "sqlite://db.sqlite3"

for plg in PLUGINS:
    globals()[lib] = __import__(plg)


async def init(**kwargs):
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"

    await Tortoise.init(db_url=DB_URL, modules={"models": PLUGINS})  # ['app.models']}
    # Generate the schema
    await Tortoise.generate_schemas()


# run_async is a helper function to run simple async Tortoise scripts.
run_async(init())
