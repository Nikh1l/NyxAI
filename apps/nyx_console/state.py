from dataclasses import dataclass
from core.chat.session import ChatSession
from core.roles.registry import RoleRegistry
from core.roles.role import Role

@dataclass
class ConsoleState:
    session: ChatSession
    role: Role
    roles: RoleRegistry