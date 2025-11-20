# **Oru — Hedera Ecosystem Intelligence Agent (HEIA)**

Oru is an autonomous intelligence agent designed for the Hedera ecosystem.  
It continuously monitors on-chain and off-chain signals, identifies trends, detects anomalies, and generates actionable insights for protocol teams and foundations.  
This project demonstrates a fast-deploy, modular, learning-capable agent architecture built for Theme 1: **AI & Agents**.

Oru is structured as reusable, production-oriented infrastructure, even if the implementation here is partial.  
This repository showcases the agent’s architecture, intelligence loop, memory layer, and operational flow.

---

## **🌐 Project Links**

All assets for judging are centralized here:

- **Pitch Deck (PDF):** `/delivrable/pitch_deck.pdf`
- **Demo Video:** `/delivrable/demo_video.mp4`
- **Figma Prototype:** `/delivrable/prototype.md`
- **Architecture Docs:** `/docs/`

No external navigation required — everything is inside the repository.

---

## **📌 Project Summary (100 words)**

Oru is an autonomous intelligence agent designed for the Hedera ecosystem.  
It continuously monitors on-chain and off-chain signals, identifies patterns, detects risks, and surfaces actionable opportunities for protocol teams and foundations.  
The agent runs on a fast-deploy containerized architecture and uses a structured intelligence loop with a lightweight memory layer to improve over time.  
Oru provides insight cards, alerts, weekly digests, and protocol-specific recommendations.  
Although designed as general-purpose intelligence infrastructure, this submission focuses on a Hedera Ecosystem Intelligence Agent that demonstrates rapid deployment, continuous learning, and high-value operational intelligence for builders across the network.

---

## **⚙️ What the Agent Does**

Oru performs 4 continuous functions:

1. **Ingestion**  
   Pulls structured and unstructured signals from Hedera Mirror Node, APIs, and optional off-chain data sources.

2. **Intelligence Loop**  
   Interprets data, detects patterns, evaluates significance, and generates insights.

3. **Memory Layer**  
   Stores past insights, user feedback, and detected patterns to improve future reasoning.

4. **Output Layer**  
   Produces:
   - opportunity insights  
   - risk alerts  
   - trend analyses  
   - weekly digest summaries  

---

## **🧱 System Architecture**

```
Data Sources (Mirror Node, APIs, Off-chain)
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
UI / API / Export (Figma demo)
```

Detailed architecture explanation is available in `/docs/architecture.md`.

---

## **📂 Repository Structure**

```
/src
    /ingestion          → Data ingestion modules (Mirror Node, APIs)
    /intelligence       → Core intelligence loop & pattern logic
    /memory             → Memory layer (insight history, patterns)
    /outputs            → Insight formatting, alert building

/infra
    hedera_config.md    → Hedera-specific setup notes
    deployment_notes.md → How the agent would be deployed (containers)

/docs
    architecture.md
    intelligence_loop.md
    memory_layer.md

/delivrable
    pitch_deck.pdf
    demo_video.mp4
    prototype.md

LICENSE
README.md
```

---

## **🚀 How to Run (Prototype Mode)**

This prototype includes code skeletons that reflect real agent structure.  
A minimal cycle can be executed by running a test script:

### **1. Install dependencies**
```
pip install -r requirements.txt
```

### **2. Run the intelligence loop test**
```
python src/intelligence/loop.py
```

### **3. Explore architecture docs**
See `/docs/architecture.md` for a full technical explanation.

---

## **🔧 Tech Stack**

- Python (agent logic, intelligence loop)
- Hedera SDK (Mirror Node ingestion)
- Docker (deployment model)
- LLM reasoning (OpenAI/Anthropic, optional)
- Figma (UI/UX prototype)
- Markdown documentation

---

## **📈 Roadmap**

### **v0.1 — Hackathon Version**
- Architecture skeleton  
- Intelligence loop prototype  
- Memory placeholder  
- Figma product demo  
- Manual ingestion examples  

### **v0.2 — Early Pilot**
- Real Mirror Node ingestion  
- Persistent memory  
- Improved pattern detection  
- Basic dashboard  

### **v0.3 — Foundation-Grade**
- Multi-protocol ingestion  
- Advanced reasoning  
- Configurable deployment templates  
- Weekly digest automation  

### **v1.0 — Production**
- Cross-chain intelligence  
- Multi-agent extensions  
- Foundation-level insights  

---

## **📄 License**

MIT License.  
See `LICENSE` for more details.

---

## **🤝 Credits**

Built by **Oru** as part of the Hedera AI & Agents Hackathon 2025.  
Designed as the foundational module for Oru’s Autonomous Protocol Intelligence Infrastructure.
