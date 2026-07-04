from core.ollama.client import OllamaClient
from core.chat.session import ChatSession
from core.config.settings import Settings
from core.roles.registry import RoleRegistry

from .commands import COMMANDS
from .state import ConsoleState

def main():
    settings = Settings()
    roles = RoleRegistry(settings)
    for role in roles.all():
        print(role)
    client = OllamaClient(settings.ollama_host)
    state = ConsoleState(
        session=ChatSession(),
        role=roles.get("assistant"),
        roles=roles
    )

    print("=" * 50)
    print("Nyx Console")
    print(f"Role: {state.role.name}")
    print(f"Model: {state.role.model}")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:
        prompt = input("\nYou > ")
        
        if prompt.startswith("/"):
            parts = prompt.split()
            command = parts[0]
            args = parts[1:]

            handler = COMMANDS.get(command)

            if handler :
                should_exit = handler(state, args)
                if should_exit :
                    print("Exiting Nyx Console.")
                    break

            else: 
                print(f"Unknown command: {command}. Type '/help' for a list of commands.")

            continue        

        state.session.add_user_message(prompt)

        assistant = ""

        print("\n🤖 ", end="", flush=True)

        for token in client.stream_chat(model=state.role.model, messages=state.session.history()):
            assistant += token
            print(token, end="", flush=True)
        
        print()

        state.session.add_assistant_message(assistant)



if __name__ == "__main__":
    main()
