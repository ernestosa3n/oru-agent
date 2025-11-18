"""
loop.py

Core intelligence loop that powers the Oru agent.
The loop handles the full cycle:
    ingest → interpret → generate insights → update memory → output.

This is a conceptual skeleton for hackathon demonstration.
"""

from .patterns import PatternDetector

class IntelligenceLoop:
    def __init__(self, ingestion, memory, output_formatter):
        self.ingestion = ingestion
        self.memory = memory
        self.output_formatter = output_formatter
        self.pattern_detector = PatternDetector()

    def run_cycle(self):
        """
        Executes a full intelligence loop cycle.
        """
        raw_data = self.ingestion.fetch()
        patterns = self.pattern_detector.detect(raw_data)
        insight = self._generate_insight(patterns)
        self.memory.store(insight)
        formatted = self.output_formatter.format(insight)
        return formatted

    def _generate_insight(self, patterns):
        """
        Converts detected patterns into structured insights.

        Returns:
            dict: structured insight object.
        """
        return {
            "id": "placeholder-id",
            "category": patterns.get("category", "trend"),
            "description": patterns.get("description", "Placeholder insight description."),
            "severity": patterns.get("severity", None),
            "confidence": patterns.get("confidence", 0.5),
            "recommended_actions": patterns.get("actions", ["Review activity."])
        }
