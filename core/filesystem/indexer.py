import ast
from pathlib import Path
from core.filesystem.collector import FileCollector

class ProjectIndexer:
    
    def __init__(self):
        self.collector = FileCollector()

    def build(self, root: str):
        index = {}

        for file in self.collector.collect(root):
            try:
                source = file.read_text(encoding="utf-8", errors="ignore")
                tree = ast.parse(source)

            except Exception:
                continue

            visitor = SymbolVisitor(file)
            visitor.visit(tree)

            for symbol in visitor.symbols:
                index.setdefault(symbol, []).append(file)

        return index
    

class SymbolVisitor(ast.NodeVisitor):
       
    def __init__(self, file: Path):
            self.file = file
            self.symbols = set()

    def visit_ClassDef(self, node):
         self.symbols.add(node.name)
         self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.symbols.add(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.symbols.add(node.name)
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.symbols.add(alias.name.split(".")[-1])

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.symbols.add(alias.name)