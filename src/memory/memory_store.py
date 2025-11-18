"""
memory_store.py

Lightweight memory layer skeleton.
In true deployments, this would be backed by:
- persistent storage
- embeddings
- pattern logs
- insight history

For hackathon purposes, a simple in-memory structure demonstrates the concept.
"""

class MemoryStore:
    def __init__(self):
        self.history = []

    def store(self, insight):
        """
        Saves insight to memory history.
        """
        self.history.append(insight)

    def get_recent(self, n=10):
        """
        Retrieves the most recent insights.
        """
        return self.history[-n:]
