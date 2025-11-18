"""
insights_formatter.py

Formats raw insight objects produced by the intelligence loop
into a clean, standardized structure suitable for:
- UI display
- export
- logging
- future API responses
"""

class InsightFormatter:
    def format(self, insight):
        """
        Formats an insight into a consistent output object.

        Args:
            insight (dict): raw structured insight.

        Returns:
            dict: formatted insight.
        """
        return {
            "insight_id": insight.get("id"),
            "category": insight.get("category"),
            "description": insight.get("description"),
            "severity": insight.get("severity"),
            "confidence": insight.get("confidence"),
            "recommended_actions": insight.get("recommended_actions"),
            "status": "generated"
        }
