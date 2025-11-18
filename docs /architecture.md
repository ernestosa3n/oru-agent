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
