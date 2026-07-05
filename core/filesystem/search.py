from pathlib import Path

from core.filesystem.collector import FileCollector
from core.filesystem.indexer import ProjectIndexer


class ProjectSearcher:

    def __init__(self):
        self.collector = FileCollector()
        self.indexer = ProjectIndexer()

        self._cache = None
        self._root = None


    def search(self, root: str, query: str, limit: int = 5):
        
        root = Path(root)

        if self._cache is None or self._root != root:
            self._cache = self.indexer.build(root)
            self._root = root
        index = self._cache

        results = []

        words = query.split()

        for word in words:
            if word in index:
                for file in index[word]:
                    if file not in results:
                        results.append(file)
                        
        if results:
            return results[:limit]
        

        # Fallback to keyword search

        matches = []

        keywords = {
            word.lower()
            for word in words
            if len(word) > 2
        }

        for file in self.collector.collect(root):

            try:
                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            except Exception:
                continue

            score = 0

            source = source.lower()

            for keyword in keywords:
                score += source.count(keyword)

            if score:
                matches.append((score, file))

        matches.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        return [
            file
            for _, file in matches[:limit]
        ]