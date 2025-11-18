# Oru — Hedera Ecosystem Intelligence Agent  
## System Architecture

This document describes the high-level architecture of the Oru agent for the Hedera ecosystem.

Oru is structured as a modular, reusable intelligence infrastructure with four main layers:

1. **Ingestion Layer** (`/src/ingestion`)  
2. **Intelligence Loop** (`/src/intelligence`)  
3. **Memory Layer** (`/src/memory`)  
4. **Output Layer** (`/src/outputs`)

---

## High-Level Diagram

```text
Data Sources (Hedera Mirror Node, APIs, Off-chain)
        │
        ▼
Ingestion Layer (/src/ingestion)
        │ normalized data
        ▼
Intelligence Loop (/src/intelligence)
        │ insights + logs
        ▼
Memory Layer (/src/memory)
        │ refined intelligence
        ▼
Output Layer (/src/outputs)
        │
        ▼
UI / API / Exports (demonstrated via Figma prototype)
```

---

## Layer Responsibilities

### 1. Ingestion Layer

- Connects to Hedera data sources (Mirror Node, HTS events, HCS messages).
- Normalizes raw data into a consistent internal structure.
- Prepares data for the intelligence loop.

Implemented conceptually in:  
`/src/ingestion/hedera_ingest.py`

---

### 2. Intelligence Loop

- Runs the main reasoning cycle of the agent:
  - fetch data  
  - detect patterns  
  - generate insights  
  - update memory  
  - format outputs  

Central logic in:  
`/src/intelligence/loop.py`  
`/src/intelligence/patterns.py`

---

### 3. Memory Layer

- Stores past insights and patterns.
- Enables the agent to improve over time.
- Provides recent context to the intelligence loop.

Implemented conceptually in:  
`/src/memory/memory_store.py`

---

### 4. Output Layer

- Formats insights into a standardized structure.
- Suitable for UI display, exports, and future APIs.
- Bridges the intelligence loop with external interfaces (dashboards, alerts, reports).

Implemented conceptually in:  
`/src/outputs/insights_formatter.py`

---

## Deployment Model (Conceptual)

In a real deployment:

- The agent would be containerized (Docker).
- Environment variables would hold configuration (Mirror Node URLs, API keys).
- A scheduler would trigger the intelligence loop periodically.
- Outputs would be exposed via:
  - API
  - dashboards
  - notifications (email, Slack/Discord, webhooks)
