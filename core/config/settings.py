from pathlib import Path
import yaml


class Settings:
    def __init__(self):
        root = Path(__file__).resolve().parents[2]
        config = root / "core" / "config" / "settings.yml"

        with open(config, "r") as f:
            self._data = yaml.safe_load(f)

    @property
    def ollama_host(self):
        return self._data["ollama"]["host"]

    @property
    def models(self):
        return self._data["models"]

    def model(self, role):
        return self._data["models"][role]

    @property
    def database_url(self):
        return self._data["database"]["url"]


settings = Settings()