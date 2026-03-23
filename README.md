# 🚀 Multimodal AI Agent System (CrewAI + MCP + Ollama)

This project demonstrates a **production-style multimodal AI system** that processes **audio and image inputs**, validates them, and generates a **grounded, structured output** using local models.

---

## 🧠 Overview

This system showcases:

- Multimodal understanding (Audio + Image)  
- Agent-based orchestration (CrewAI)  
- Tool execution via MCP  
- Local-first AI (Ollama + Whisper, no API keys)  
- Grounded reasoning with validation  

---

## 🏗️ Architecture

User Inputs (Audio + Image)  
↓  
CrewAI Agents (Reasoning Layer)  
↓  
MCP Server (Execution Layer)  
↓  
Tools (Whisper, Moondream, Validation)  
↓  
Final Structured Output  

---

## ⚙️ Tech Stack

- CrewAI  
- MCP (FastAPI)  
- Ollama (phi3, moondream)  
- Whisper  
- Python  

---

## 📁 Project Structure

```
multimodal_agent/
├── main.py
├── agents.py
├── tasks.py
├── tools.py
├── mcp_server.py
├── mcp_client.py
├── inputs/
│   ├── earth.jpg
│   └── moon.wav
└── README.md
```

---

## ▶️ How to Run

### 1. Activate environment
```
conda activate crewmcp2
```

### 2. Start Ollama
```
ollama run phi3
```

### 3. Start MCP Server
```
uvicorn mcp_server:app --port 9000 --reload
```

### 4. Run project
```
python main.py
```

---

## 📤 Output

```
{
  "answer": "...",
  "audio_transcript": "...",
  "image_description": "...",
  "confidence": 0.9,
  "evidence": [...],
  "uncertainty": "low"
}
```

---

## 🔍 Key Features

- Multimodal processing  
- Agent-based workflow  
- MCP execution layer  
- Grounded AI outputs  

---

## ⚠️ Requirements

- Python 3.10+
- FFmpeg
- Ollama installed

---

## ✍️ Medium Blog

Read the full blog here:  
https://medium.com/@your-username/multimodal-ai-agents-crewai-mcp-ollama

---

## 🚀 Future Work

- Video understanding  
- Streaming  
- API deployment  
- UI integration  

---

## 📜 License

MIT License

---

## 🔥 Final Thought

The future of AI isn’t just smarter models—it’s better systems.
