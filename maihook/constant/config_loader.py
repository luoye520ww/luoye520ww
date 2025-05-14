import json
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self._data = None
        self.load()
    
    def load(self):
        with open(self.config_path, 'r', encoding='utf-8') as f:
            self._data = json.load(f)
    
    @property
    def mai_config(self) -> dict:
        return self._data["mai_config"]
    
    @property
    def plate_to_version(self) -> list:
        return self._data["plate_to_version"]
    
    @property
    def id_to_region(self) -> list:
        return self._data["id_to_region"]


mai_config = load_config()