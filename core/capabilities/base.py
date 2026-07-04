from pathlib import Path

from core.ollama.client import OllamaClient
from core.prompts.loader import PromptLoader
from core.roles.role import Role

class BaseCapability:
    
    def __init__(self, client: OllamaClient, role: Role):
        self.client = client
        self.role = role

    def load_prompt(self, path: Path) -> str:
        return PromptLoader.load(path)
    
    def stream(self, messages):
        return self.client.stream_chat(self.role.model, messages)
    
    def chat(self, messages):
        return self.client.chat(self.role.model, messages)
