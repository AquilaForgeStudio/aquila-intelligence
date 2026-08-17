import json
from pathlib import Path

CONFIG_DIR = Path(__file__).parent

with open(CONFIG_DIR / "ui.json", "r", encoding="utf-8") as f:
    UI_CONFIG = json.load(f)