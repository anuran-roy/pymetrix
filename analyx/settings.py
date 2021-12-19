import sys

from pathlib import Path

PACK_BASE = str(Path(__file__).resolve().parent)


def set_path():
    if PACK_BASE in sys.path:
        print(sys.path)
    else:
        sys.path.append(PACK_BASE)


DEBUG = True
VERBOSE = True

PLUGINS = [
    "test_plugin",
]
