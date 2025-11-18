# Intelligence Loop — Oru Hedera Agent

The intelligence loop is the core of the Oru agent.  
It is responsible for turning raw data into structured, actionable insights.

---

## Loop Overview

The loop follows a simple but powerful cycle:

1. **Ingest** — pull data from Hedera and optional off-chain sources.  
2. **Detect** — analyze data and extract meaningful patterns.  
3. **Generate** — convert patterns into structured insights.  
4. **Store** — write insights into the memory layer.  
5. **Format** — prepare insights for UI/API consumption.

This cycle can be run periodically (e.g. hourly, daily) or triggered on demand.

---

## Code Skeleton

The loop is implemented conceptually in:

`/src/intelligence/loop.py`

```python
class IntelligenceLoop:
    def run_cycle(self):
        raw_data = self.ingestion.fetch()
        patterns = self.pattern_detector.detect(raw_data)
        insight = self._generate_insight(patterns)
        self.memory.store(insight)
        formatted = self.output_formatter.format(insight)
        return formatted
```

---

## Pattern Detection

Pattern detection is abstracted into:

`/src/intelligence/patterns.py`

Responsibilities include:

- detecting unusual activity  
- basic anomaly identification  
- extracting ecosystem signals  
- returning a compact pattern summary for the loop  

---

## Insight Structure

The loop generates an insight object containing fields such as:

- **category** (opportunity, risk, trend)  
- **description**  
- **severity**  
- **confidence**  
- **recommended_actions**

This ensures insights remain standardized and usable across different outputs.

---

## Future Extensions

In a full implementation, the intelligence loop may include:

- LLM-based reasoning  
- statistical anomaly detection  
- protocol-specific heuristics  
- user feedback integration  
- multi-agent coordination  

The current skeleton remains intentionally lightweight for the hackathon while demonstrating a strong architectural foundation.
