# 🤖 Multi-Agent AI Suite — Streamlit App

A modular multi-agent application built with Streamlit, OpenAI GPT and Perplexity API.  
Each agent is specialized for a specific business use case and can be extended independently.

---

## 🎯 Key Features

- **Modular architecture** — add a new agent by simply creating a `config_agent_xxx.py` file
- **Two-step AI pipeline** — Perplexity handles real-time research, OpenAI handles structured writing
- **Configurable parameters** — model, temperature, max tokens adjustable directly from the UI
- **Built-in documentation tab** — parameter recommendations per agent type

---

## 🧠 Available Agents

### 💼 Agent Investisseur
Specialized in investment analysis for real estate and emerging markets (notably Africa).  
Produces structured executive reports including:
- Macroeconomic context
- Market analysis (supply/demand, yields, prices)
- Growth drivers & opportunities
- Risk assessment (low / moderate / high)
- 3 investment scenarios (optimistic / central / pessimistic)
- Final verdict: Investable / Investable under conditions / Avoid

### 📰 Agent Presse & Contenu Digital
Specialized in digital content creation and SEO/GEO optimization.  
Produces:
- LinkedIn posts (News / Trends / Strategic advice formats)
- SEO+GEO web articles (400–600 words)
- Weekly editorial strategies

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| Research | Perplexity API (sonar-pro) |
| Writing | OpenAI API (GPT-4o / GPT-5) |
| Language | Python 3.10+ |
| Architecture | Modular agent config files |

---

## 🚀 Installation & Usage

### 1. Clone the repo
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API keys
```bash
cp .env.example .env
```
Then fill in your keys in `.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
PERPLEXITY_API_KEY=your_perplexity_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Use the app
- Select an agent from the sidebar
- Enter your API keys (or configure via `st.secrets`)
- Adjust AI parameters (model, temperature, max tokens)
- Enter your topic and click the generate button

---

## 📁 Project Structure

```
├── app.py                          # Main Streamlit app & orchestration
├── agents/
│   ├── __init__.py
│   ├── config_agent_investisseur.py   # Investment analysis agent
│   ├── config_agent_presse.py         # Press & digital content agent
│   └── config_agent_X_template.py     # Template to create a new agent
├── agent_api_connection_exemple.py    # Basic pipeline example
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ➕ Adding a New Agent

1. Create a new file `agents/config_agent_yourname.py`
2. Define the required variables:
```python
AGENT_NAME = "Your Agent Name"
AGENT_ICON = "🔥"
AGENT_DESCRIPTION = "What this agent does."
INPUT_TITLE = "Section title"
INPUT_LABEL = "Input label"
INPUT_PLACEHOLDER = "Example input..."
BUTTON_LABEL = "Generate"

def build_agent_prompt(topic: str, research_text: str, sources: str) -> str:
    return f"Your prompt here... {topic} {research_text} {sources}"
```
3. The app auto-discovers it — no other changes needed ✅

---

## 👤 Author

**Hippolyte Inthivong**  
AI Engineer | Predictive Models & Data Pipelines  
[LinkedIn](https://www.linkedin.com/in/hippolyte-inthivong-295210214)
