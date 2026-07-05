from pathlib import Path
from core.capabilities.base import BaseCapability
from core.filesystem.collector import FileCollector
from core.filesystem.context import FileContext
from core.filesystem.search import ProjectSearcher


class EngineerCapability(BaseCapability):

    def __init__(self, client, role):
        super().__init__(client, role)
        self.prompt_dir = Path(__file__).parent / "prompts"
        self.searcher = ProjectSearcher()

    def _execute(self, prompt_name: str, context: str):
        prompt = self.load_prompt(
            self.prompt_dir / f"{prompt_name}.md"
        )

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


    def explain(self, target: str):
        target = Path(target)
        collector = FileCollector()

        if target.is_dir():
            files = collector.collect(target)
            context = FileContext.from_files(files)
        else:
            context = FileContext.from_file(target)

        return self._execute("explain", context)

    
    def review(self, file_path: str):
        return self._execute("review", file_path)


    def tests(self, file_path: str):
        return self._execute("tests", file_path)
    

    def ask(self, project_root: str, question: str):

        files = self.searcher.search(project_root, question)
        context = FileContext.from_files(files)
        prompt = f"""
    Question

    {question}

    Project Context

    {context}
    """
        
        return self._execute("ask", prompt)
    
    
    def search(self, project_root: str, query: str):

        return self.searcher.search(
            project_root,
            query,
        )