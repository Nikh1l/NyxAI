from core.chat.session import ChatSession
from core.config.settings import Settings
from core.ollama.client import OllamaClient
from core.roles.registry import RoleRegistry
from core.capabilities.engineer.capability import EngineerCapability

from .commands import COMMANDS
from .state import ConsoleState
from .ui import capability_banner

def stream_response(stream, state):
    assistant_message = ""

    print("\n🤖 ", end="", flush=True)

    for token in stream:
        assistant_message += token
        print(token, end="", flush=True)

    print()

    state.session.add_assistant_message(assistant_message)


def main():

    settings = Settings()

    roles = RoleRegistry(settings)

    client = OllamaClient(settings.ollama_host)

    state = ConsoleState(
        session=ChatSession(),
        role=roles.get("assistant"),
        roles=roles
    )

    engineer = EngineerCapability(
        client,
        roles.get("engineer")
    )

    print("=" * 50)
    print("Nyx Console")
    print(f"Role: {state.role.name}")
    print(f"Model: {state.role.model}")
    print("Type '/help' for commands.")
    print("=" * 50)

    while True:

        prompt = input(f"\n[{state.role.name}] > ").strip()

        if not prompt:
            continue


        # -----------------------------
        # Slash Commands
        # -----------------------------
        if prompt.startswith("/"):

            parts = prompt.split()

            command = parts[0]
            args = parts[1:]

            handler = COMMANDS.get(command)

            if handler:

                should_exit = handler(state, args)

                if should_exit:
                    break

            else:
                print(f"Unknown command: {command}")

            continue

        # -----------------------------
        # Capability Commands
        # engineer explain file.py
        # engineer review file.py
        # engineer tests file.py
        # -----------------------------
        parts = prompt.split(maxsplit=2)

        parts = prompt.split(maxsplit=2)

        if len(parts) >= 2:

            capability = parts[0]
            action = parts[1]

            if capability == "engineer":

                if action == "ask":

                    if len(parts) != 3:
                        print("Usage: engineer ask <question>")
                        continue

                    question = parts[2]

                    capability_banner(
                        capability,
                        action,
                        question,
                    )

                    stream = engineer.ask(
                        ".",
                        question,
                    )

                else:

                    if len(parts) != 3:
                        print(f"Usage: engineer {action} <path>")
                        continue

                    target = parts[2]

                    capability_banner(
                        capability,
                        action,
                        target,
                    )

                    if action == "explain":
                        stream = engineer.explain(target)

                    elif action == "review":
                        stream = engineer.review(target)

                    elif action == "tests":
                        stream = engineer.tests(target)

                    elif action == "search":
                        if len(parts) != 3:
                            print("Usage: engineer search <query>")
                            continue
                        files = engineer.search(".", parts[2])
                        print()
                        for file in files:
                            print(file)
                        continue

                    else:
                        print(f"Unknown engineer action: {action}")
                        continue

                stream_response(stream, state)
                continue

        # -----------------------------
        # Normal Chat
        # -----------------------------
        state.session.add_user_message(prompt)

        stream = client.stream_chat(
            model=state.role.model,
            messages=state.session.history(),
        )

        stream_response(stream, state)




if __name__ == "__main__":
    main()
