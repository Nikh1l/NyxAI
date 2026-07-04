from core.ollama.client import OllamaClient
from core.chat.session import ChatSession
from .config import DEFAULT_MODEL
from .commands import COMMANDS


def main():
    client = OllamaClient()
    session = ChatSession()

    print("=" * 50)
    print("Nyx Console")
    print(f"Model: {DEFAULT_MODEL}")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:
        prompt = input("\nYou > ")
        
        if prompt.startswith("/"):
            command = prompt.split()[0]
            if command in COMMANDS:
                action = COMMANDS[command]
                if action == "show_help":
                    print("\nAvailable commands:")
                    for cmd in COMMANDS:
                        print(f"  {cmd}")
                elif action == "clear_chat":
                    session.clear()
                    print("\nChat history cleared.")
                elif action == "show_model":
                    print(f"\nCurrent model: {DEFAULT_MODEL}")
                elif action == "exit_console":
                    print("\nExiting Nyx Console. Goodbye!")
                    break
            else:
                print(f"\nUnknown command: {command}. Type '/help' for a list of commands.")
            continue

        session.add_user_message(prompt)

        assistant = ""

        print("\nNyxAI is thinking...", end="", flush=True)

        for chunk in client.stream_chat(model=DEFAULT_MODEL, messages=session.history()):
            if chunk.get("done"):
                break
            token = chunk["message"]["content"]
            assistant += token
            print(token, end="", flush=True)
        
        print()

        session.add_assistant_message(assistant)



if __name__ == "__main__":
    main()
