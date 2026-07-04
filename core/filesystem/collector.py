from pathlib import Path

class FileCollector:

    DEFAULT_EXTENSIONS = {".py"}
    
    DEFAULT_IGNORE = {
        ".git",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".idea",
        ".vscode",
        "node_modules",
    }

    def __init__(self, extensions=None, ignore=None):
        self.extensions = extensions or self.DEFAULT_EXTENSIONS
        self.ignore = ignore or self.DEFAULT_IGNORE


    def collect(self, root: str):

        root = Path(root)

        files = []

        for file in root.rglob("*"):
            
            if not file.is_file():
                continue

            if file.suffix not in self.extensions:
                continue 

            if any(part in self.ignore for part in file.parts):
                continue

            files.append(file)

        return sorted(files)