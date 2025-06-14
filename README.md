
<h1 align="center">🤖 RECAP: Agentic AI System for Pitch Evaluation</h1>

<p align="center">
A multi-agent system for entrepreneurs to refine startup pitch presentations powered by LangGraph, LangChain, and Gemini Pro.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Overview-blue" />
  <img src="https://img.shields.io/badge/Motivation-lightgrey" />
  <img src="https://img.shields.io/badge/System_Overview-green" />
  <img src="https://img.shields.io/badge/Modules-orange" />
  <img src="https://img.shields.io/badge/Tech_Stack-yellow" />
  <img src="https://img.shields.io/badge/Project_Structure-purple" />
  <img src="https://img.shields.io/badge/Getting_Started-brightgreen" />
  <img src="https://img.shields.io/badge/API_Usage-blueviolet" />
  <img src="https://img.shields.io/badge/Docker_Deployment-ff69b4" />
  <img src="https://img.shields.io/badge/Roadmap-critical" />
  <img src="https://img.shields.io/badge/License-informational" />
  <img src="https://img.shields.io/badge/Contact-success" />
</p>


---


**RECAP** (Review Engine for Critiquing and Advising Pitches) is an LLM-powered agentic system designed to help founders and entrepreneurs receive **actionable**, **multi-perspective**, and **structured feedback** on their startup pitch presentations.

Leveraging Gemini Pro via `langchain-google-genai`, RECAP orchestrates multiple autonomous agents through `LangGraph` to simulate feedback from expert investors, mentors, and communication coaches.

---

## 🧠 Motivation

Delivering a compelling pitch is vital for fundraising, networking, and market traction. However, high-quality, domain-relevant feedback is often:

- ❌ Expensive
- ❌ Inconsistent
- ❌ Inaccessible at scale

**RECAP bridges this gap** by delivering fast, repeatable, and context-aware AI evaluations — personalized for your niche and audience.

---

## ⚙️ System Overview

> A multi-agent LLM system orchestrated through LangGraph for synchronous evaluation.

### Highlights:

- 🧩 **Autonomous agents** for speech, content, and judgment.
- 🧠 **Advanced prompt templates** with expert prompting techniques.
- 🔄 **Graph-based execution flow** using `LangGraph`.
- 🧾 **Typed feedback** with `Pydantic v2` schemas.
- 🤖 **Powered by Gemini Pro** via LangChain's `langchain-google-genai` wrapper.

---

## 🧩 Modules

| Agent         | Role                                                                 |
|---------------|----------------------------------------------------------------------|
| 🗣 `SpeechAgent`  | Evaluates clarity, confidence, pacing, and delivery.                |
| 📄 `ContentAgent` | Assesses business clarity, market opportunity, and scalability.     |
| 🧑‍⚖️ `JudgeAgent`   | Emulates investor/judge perspective based on the target audience. |
| 🧷 `Combiner`     | Aggregates results and compiles cohesive final feedback.           |

Each agent acts independently and their outputs are merged for a comprehensive review.

---

## 🛠 Technology Stack

| Layer             | Framework / Tooling                         |
|-------------------|---------------------------------------------|
| Language Model    | Gemini Pro via `langchain-google-genai`     |
| Orchestration     | `LangGraph` for agent workflow management    |
| Prompt Engineering| `LangChain` with structured `PromptTemplate` |
| Backend API       | `FastAPI` for REST endpoints                |
| Data Modeling     | `Pydantic v2` for schema enforcement         |
| Environment Mgmt  | [`uv`](https://github.com/astral-sh/uv)     |
| Deployment        | `Docker`, `Docker Compose`, `Uvicorn`       |

---

## 📁 Project Structure

```bash
RECAP/
├── agents/               # LangChain agents (speech, content, judge)
├── core/                 # State schema, config, and feedback combiner
├── api/                  # FastAPI server entrypoint
├── pitch.py              # CLI entry for local testing
├── pyproject.toml        # Project metadata and dependencies
├── Dockerfile            # Image specification
├── docker-compose.yml    # Docker orchestration
└── README.md             # Project documentation
````

---

## 🚀 Getting Started

### Prerequisites

* Python 3.11+
* [`uv`](https://github.com/astral-sh/uv)
* Google Gemini API Key

### Setup

```bash
git clone https://github.com/SYED-M-HUSSAIN/RECAP.git
cd RECAP

# Create virtual environment
uv venv
source .venv/bin/activate

# Install all dependencies
uv pip install -e .

# Add your Gemini key
echo "GOOGLE_API_KEY=your-key" > .env
```

---

## ▶️ API Usage

Start the FastAPI server:

```bash
uvicorn api.main:app --reload
```

Open the interactive API at: [http://localhost:8000/docs](http://localhost:8000/docs)

### Example cURL:

```bash
curl -X POST http://localhost:8000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "transcript": "Hi, I am Sarah from MedLink...",
    "niche": "HealthTech",
    "audience": "Investor"
  }'
```

Response includes structured feedback from all agents.

---

## 📦 Docker Deployment

```bash
docker compose up --build
```

Runs RECAP inside a production-ready container with FastAPI and all agents activated.

---

## 🧭 Roadmap

* 🎙️ Speech-to-Text input via Whisper or Gemini Multimodal
* 🌍 Support for multilingual evaluation and regional investor expectations
* 📊 Performance dashboard with pitch history and iteration tracking
* 🔁 Integration with pitch practice platforms
* 🧠 Plugin-based custom agent extensions (storytelling, emotion, etc.)

---

## 📜 License

This project is licensed under the MIT License.
See [`LICENSE`](./LICENSE) for more details.

---

## 🙌 Acknowledgments

RECAP is built on top of world-class open-source libraries:

* [LangGraph](https://github.com/langchain-ai/langgraph)
* [LangChain](https://github.com/langchain-ai/langchain)
* [Google Gemini Pro](https://ai.google.dev/)
* [langchain-google-genai](https://github.com/langchain-ai/langchain-google-genai)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Pydantic](https://docs.pydantic.dev/)
* [uv](https://github.com/astral-sh/uv)

---

## 💼 Contact

**Author:** [Syed Muhammad Hussain](https://www.linkedin.com/in/syed-muhammad-hussain-00b2a7214/)
**Email:** [hs2764641@gmail.com](mailto:hs2764641@gmail.com)


