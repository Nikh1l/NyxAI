from core.roles.registry import RoleRegistry
from .state import ConsoleState

def help_command(state: ConsoleState, roles: RoleRegistry):
    print("\nAvailable commands:")
    print("  /help")
    print("  /clear")
    print("  /role")
    print("  /exit")


def clear_command(state: ConsoleState, roles: RoleRegistry):
    state.session.clear()
    print("Conversation cleared.")


def exit_command(state: ConsoleState, roles: RoleRegistry):
    return True


def role_command(state: ConsoleState, args):
    if len(args) != 1:
        print("Usage: /role <role_name>")
        return

    role_name = args[0].lower()

    role = state.roles.get(role_name)

    if role is None:
        print(f"Role '{role_name}' not found.")
        print("Available roles:")

        for r in state.roles.all():
            print(f"  {r.name}")

        return

    state.role = role
    state.session.clear()

    print(f"Role changed to: {state.role.name}")
    print("Started a new conversation.")


COMMANDS = {
    "/help": help_command,
    "/clear": clear_command,
    "/exit": exit_command,
    "/role": role_command,
}