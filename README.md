# 🟣 VEXAI | The Ultimate Hybrid Intelligence
**Developed by Not_Da4k**

VEXAI is a high-performance AI interface that leverages the power of Ollama to bring a professional, enterprise-grade experience to your local machine. Featuring the "Voidcraft" aesthetic and a multi-engine synthesis architecture.

## 🚀 Features
- **Multiverse Engine:** Switch between Speed, Scholar, Elite, and God-tier models.
- **Enterprise UI:** Professional Glassmorphism and Cinematic design.
- **Identity Lock:** Hard-coded persona ensuring absolute loyalty to Not_Da4k.
- **Local & Private:** Runs entirely on your hardware via Ollama.

## 🛠️ Installation

### 1. Prerequisites
- **Install Ollama:** Download from [ollama.com](https://ollama.com)
- **Install Python:** Download from [python.org](https://python.org) (3.10 or higher recommended)
- One cmd installing
- pip install streamlit requests; @("treyleo16/haiku-4-5","treyleo16/mythos-5","treyleo16/fable-5-1","treyleo16/sonnet-5","treyleo16/gpt-5-6-terra","treyleo16/gpt-6-astra") | % { ollama pull $_ }; python -m streamlit run vexai_ultimate.py
(note this will only work when you have installed python and ollama)

### 2. Model Setup
Open your terminal and pull the required engines:
```bash
ollama pull treyleo16/haiku-4-5:latest
ollama pull treyleo16/mythos-5:latest
ollama pull treyleo16/fable-5-1:latest
ollama pull treyleo16/sonnet-5:latest
ollama pull treyleo16/gpt-5-6-terra:latest
ollama pull treyleo16/gpt-6:latest
git clone https://github.com/darknessyt749-afk/VEX.AI.git
cd VEXAI
pip install -r requirements.txt
python -m streamlit run vexai_ultimate.py
Initialization Complete. Welcome to the Multiverse. Enjoy the power, provided by Not_Da4k
