from pathlib import Path
from core.capabilities.base import BaseCapability
from core.filesystem.collector import FileCollector
from core.filesystem.context import FileContext


class EngineerCapability(BaseCapability):

    def __init__(self, client, role):
        super().__init__(client, role)
        self.prompt_dir = Path(__file__).parent / "prompts"

    def _execute(self, prompt_name: str, target: str):

        target = Path(target)

        prompt = self.load_prompt(
            self.prompt_dir / f"{prompt_name}.md"
        )

        collector = FileCollector()

        if target.is_dir():
            files = collector.collect(target)
            context = FileContext.from_files(files)

        else:
            context = FileContext.from_file(target)

        print(f"Prompt: {prompt_name}")
        print(f"Context: {context}")

        messages = [
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": context,
            },
        ]

        return self.stream(messages)

    def explain(self, file_path: str):
        return self._execute("explain", file_path)

    def review(self, file_path: str):
        return self._execute("review", file_path)

    def tests(self, file_path: str):
        return self._execute("tests", file_path)