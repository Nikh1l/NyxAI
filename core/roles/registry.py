from core.config.settings import Settings
from core.roles.role import Role

class RoleRegistry:

    def __init__(self, settings: Settings):
        self._roles = {}
        
        for name, model in settings.models.items():
            self._roles[name] = Role(
                name=name,
                model=model["model"],
            )

    def get(self, name: str) -> Role:
        return self._roles.get(name)
    

    def all(self):
        return list(self._roles.values())