import json
from pathlib import Path


def load_config(file_path: Path) -> dict:
    with open(file_path, "r") as file:
        return json.load(file)
