import json

from utils import resource


USERDATA_PATH = resource.resource_path("data", "private", "userdata.json")

with open(USERDATA_PATH, "r", encoding="utf-8") as f:
    USERDATA = json.load(f)


UI_CONFIG_PATH = resource.resource_path("config", "ui.json")

with open(UI_CONFIG_PATH, "r", encoding="utf-8") as f:
    UI_CONFIG = json.load(f)