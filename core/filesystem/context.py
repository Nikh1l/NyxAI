from pathlib import Path

class FileContext:

    @staticmethod
    def from_file(path: Path):
        source = path.read_text(encoding="utf-8", errors="ignore")
        return f"""
File:
{path}

Language:
Python

Source:
```python
{source}
```
"""
    
    @staticmethod
    def from_files(files):
        return "\n\n".join(FileContext.from_file(file) for file in files)