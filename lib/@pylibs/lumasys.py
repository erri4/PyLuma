from LumaExtBundle import Raw
import os
import json

path = "C:/PyLuma"

if os.name == "nt":
    path = "C:/PyLuma"
elif os.name == "posix":
    path = os.path.expanduser("~/PyLuma")

path = os.path.join(path, 'version.json')

with open(path) as f:
    version = json.load(f)['version']

LumaExtension = {
    "version": {
        "type": "str",
        "name": "version",
        "args": [Raw(version)],
    },
}
