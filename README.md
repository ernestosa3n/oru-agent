# **Oru — Hedera Ecosystem Intelligence Agent (HEIA)**

Oru is an autonomous intelligence agent designed specifically for the Hedera ecosystem.  
It continuously monitors on-chain and off-chain signals, detects anomalies, identifies trends, and surfaces actionable insights for protocol teams and foundations.

This submission demonstrates a fast-deploy, modular, learning-capable agent architecture built for **Theme 1: AI & Agents**, with emphasis on verifiable agent logic and ecosystem-level intelligence.

Although the implementation is partially simulated, the system architecture, intelligence loop, memory model, and UX prototype reflect a production-oriented infrastructure approach.

---

## **🌐 Hackathon Deliverables (Centralized)**

| Deliverable | Link |
|------------|------|
| 🧩 **Interactive Figma Prototype** | `/deliverables/prototype.md` |
| 🎬 **Demo Video** | `/deliverables/demo_video.mp4` |
| 📑 **Pitch Deck (PDF)** | `/deliverables/pitch_deck.pdf` |
| 📘 **Architecture Docs** | `/docs/` |

All judging material is stored inside the repository.  
No external navigation required.

---

## **📌 Project Summary (100 words)**

Oru is an autonomous intelligence agent built for the Hedera ecosystem.  
It ingests on-chain and off-chain signals, detects meaningful patterns, identifies risks, and surfaces ecosystem opportunities for protocol teams and foundation operators.  
The agent runs on a fast-deploy, container-ready architecture and uses a structured intelligence loop with a lightweight memory layer to improve over time.  
This prototype demonstrates a Hedera Ecosystem Intelligence Agent using simulated ingestion, real agent logic, and a production-grade UX.  
It highlights rapid deployment, continuous learning, and high-value operational intelligence for builders across the network.

---

## **⚙️ What the Agent Does**

Oru performs four continuous intelligence functions:

1. **Ingestion**  
   Pulls structured and unstructured signals from Hedera Mirror Node, APIs, and optional off-chain sources.

2. **Intelligence Loop**  
   Detects anomalies, evaluates patterns, and produces structured insights.

3. **Memory Layer**  
   Stores insights, patterns, timestamps, and reasoning traces to improve the next evaluation cycle.

4. **Output Layer**  
   Generates:  
   - opportunity insights  
   - risk alerts  
   - trend analyses  
   - digest-style summaries  

---

## **🧱 System Architecture**

Data Sources (Mirror Node, APIs, Off-chain)
│
▼

Ingestion Layer (/src/ingestion)
│ normalized data
▼

Intelligence Loop (/src/intelligence)
│ insights + reasoning + logs
▼

Memory Layer (/src/memory)
│ reinforced patterns
▼

Output Layer (/src/outputs)
│
▼

UI / API / Export (Figma Prototype)

Detailed explanations available in `/docs/architecture.md`.

---

## **📂 Repository Structure**
/src
/ingestion          → Hedera ingestion mock modules
/intelligence       → Core intelligence loop & pattern logic
/memory             → Memory layer (insight history, patterns)
/outputs            → Insight formatting, alert builders

/infra
hedera_config.md    → Hedera SDK & environment notes
deployment_notes.md → Deployment model (containers, services)

/docs
architecture.md
intelligence_loop.md
memory_layer.md

/deliverables
pitch_deck.pdf
demo_video.mp4
prototype.md

LICENSE
README.md
---

## **🚀 Running the Prototype Code**

This project includes a minimal runnable skeleton to illustrate the agent’s internal flow.

### **1. Install dependencies**
pip install -r requirements.txt

### **2. Run an intelligence loop cycle**
python src/demo_run.py

### **3. Explore documentation**
See `/docs/` for architecture and module explanations.

---

## **🔧 Tech Stack**

- Python (agent logic)
- Hedera SDK (Mirror Node ingestion model)
- Docker (deployment approach)
- LLM reasoning (optional)
- Markdown documentation
- Figma (high-fidelity UX prototype)

---

## **📈 Roadmap**

### **v0.1 — Hackathon Version**
- Architecture skeleton  
- Intelligence loop prototype  
- Memory placeholder  
- Figma demo  
- Simulated ingestion  

### **v0.2 — Early Pilot**
- Real Mirror Node ingestion  
- Pattern detection improvements  
- Persistent memory  
- Basic dashboard backend  

### **v0.3 — Foundation-Grade**
- Multi-protocol support  
- Advanced reasoning logic  
- Configurable deployment templates  
- Weekly digest automation  

### **v1.0 — Production**
- Cross-chain intelligence  
- Multi-agent orchestration  
- Enterprise-grade insights  

---

## **📄 License**

MIT License.  
See `LICENSE` for more details.

---

## **🤝 Credits**

Built by **Oru** for the Hedera AI & Agents Hackathon 2025.  
This module is the foundation of Oru’s long-term vision:  
**Autonomous Protocol Intelligence Infrastructure.**
