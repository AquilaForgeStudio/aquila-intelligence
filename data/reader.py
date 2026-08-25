import json
from pathlib import Path

DATA_DIR = Path(__file__).parent

with open(DATA_DIR / "private/userdata.json", "r", encoding="utf-8") as f:
    USERDATA = json.load(f)