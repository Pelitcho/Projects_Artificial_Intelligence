import os
import importlib
import requests
import streamlit as st
from openai import OpenAI
import sys

# ==============================================
# 1. FONCTION D’EXTRACTION GPT UNIFIÉE
# ==============================================
def extract_gpt_content(msg):
    if isinstance(msg.content, str):
        return msg.content

    if isinstance(msg.content, list):
        texts = []
        for block in msg.content:
            if isinstance(block, dict):
                if "text" in block:
                    texts.append(block["text"])
                elif "content" in block:
                    texts.append(block["content"])
        if texts:
            return "\n".join(texts)

    if hasattr(msg, "text") and isinstance(msg.text, str):
        return msg.text

    if hasattr(msg, "output_text") and isinstance(msg.output_text, str):
        return msg.output_text

    if hasattr(msg, "delta") and isinstance(msg.delta, dict):
        return msg.delta.get("text", "")

    return ""

# ==============================================
# 2. CONFIG STREAMLIT
# ==============================================
st.set_page_config(
    page_title="Multi-Agent Suite",
    page_icon="🤖",
    layout="wide",
)

# ==============================================
# 3. DÉCOUVERTE DES CONFIG AGENTS
# ==============================================
AGENT_FOLDER = "agents"

available_agents = [
    f.replace(".py", "")
    for f in os.listdir(AGENT_FOLDER)
    if f.startswith("config_agent_") and f.endswith(".py")
]

# ==============================================
# 4. SIDEBAR : CHOIX AGENT + PARAMÈTRES
# ==============================================
with st.sidebar:
    st.title("🧩 Choix de l’agent")
    selected_agent = st.selectbox("Sélectionne l’agent :", available_agents)

    st.header("🔐 API Keys")
    pplx_key = st.text_input("Perplexity API Key", type="password")
    openai_key = st.text_input("OpenAI API Key", type="password")

    st.subheader("🧠 Paramètres IA")
    pplx_model = st.text_input("Modèle Perplexity", value="sonar-pro")
    openai_model = st.text_input("Modèle OpenAI", value="gpt-5.1")
    temperature = st.slider("Creativité", 0.0, 1.5, 0.7)
    max_tokens = st.slider("Max Tokens", 512, 4096, 2000)

# ==============================================
# 5. RECHARGEMENT DYNAMIQUE DE L’AGENT
# ==============================================
module_path = f"{AGENT_FOLDER}.{selected_agent}"
if module_path in sys.modules:
    del sys.modules[module_path]

config_module = importlib.import_module(module_path)

AGENT_NAME = config_module.AGENT_NAME
AGENT_ICON = config_module.AGENT_ICON
AGENT_DESCRIPTION = config_module.AGENT_DESCRIPTION
INPUT_TITLE = config_module.INPUT_TITLE
INPUT_LABEL = config_module.INPUT_LABEL
INPUT_PLACEHOLDER = config_module.INPUT_PLACEHOLDER
BUTTON_LABEL = config_module.BUTTON_LABEL
build_agent_prompt = config_module.build_agent_prompt

# ==============================================
# 6. API PERPLEXITY
# ==============================================
def call_perplexity_text(query, api_key, model="sonar-pro"):
    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "stream": False,
        "messages": [
            {"role": "system", "content": "You are a research engine providing structured data."},
            {"role": "user", "content": query},
        ],
    }
    response = requests.post(url, json=payload, headers=headers, timeout=500)
    response.raise_for_status()
    data = response.json()
    return data.get("choices", [{}])[0].get("message", {}).get("content", "")

def call_perplexity_sources(query, api_key, model="sonar-pro"):
    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "stream": False,
        "messages": [
            {"role": "system", "content": "You are a research engine providing structured data."},
            {"role": "user", "content": query},
        ],
    }
    response = requests.post(url, json=payload, headers=headers, timeout=500)
    response.raise_for_status()
    return response.json().get("citations", [])

# ==============================================
# 7. API OPENAI (GPT-5 / GPT-5-nano compatible)
# ==============================================
def call_openai_agent(topic, research_text, sources_clean):
    client = OpenAI(api_key=openai_key)
    prompt = build_agent_prompt(topic, research_text, sources_clean)

    completion = client.chat.completions.create(
        model=openai_model,
        temperature=temperature,
        max_completion_tokens=max_tokens,
        messages=[
            {"role": "system", "content": "You are an expert in managing text to be structured and clear."},
            {"role": "user", "content": prompt},
        ],
    )

    return extract_gpt_content(completion.choices[0].message)

# ==============================================
# 8. TABS UI
# ==============================================
tab_agent, tab_doc = st.tabs(["🤖 Agent", "📘 Documentation"])

# ==============================================
# 9. ONGLET 1 – AGENT
# ==============================================
with tab_agent:

    st.markdown(f"<div class='big-title'>{AGENT_ICON} {AGENT_NAME}</div>", unsafe_allow_html=True)
    st.write(AGENT_DESCRIPTION)

    st.subheader(INPUT_TITLE)
    topic = st.text_input(INPUT_LABEL, placeholder=INPUT_PLACEHOLDER, key=f"input_{selected_agent}")

    if st.button(BUTTON_LABEL, key=f"btn_{selected_agent}"):
        if not pplx_key or not openai_key:
            st.error("❌ Merci de renseigner les clés API.")
            st.stop()

        if not topic.strip():
            st.error("❌ Merci d’indiquer un sujet.")
            st.stop()

        with st.spinner("🔎 Recherche Perplexity…"):
            pplx_text = call_perplexity_text(topic, pplx_key, pplx_model)

        with st.spinner("📚 Extraction des sources…"):
            citations = call_perplexity_sources(topic, pplx_key, pplx_model)

        sources_clean = "\n".join([f"- {c}" for c in citations]) or \
                         "Sources non précisées par Perplexity."

        with st.spinner("🧠 Analyse OpenAI…"):
            output = call_openai_agent(topic, pplx_text, sources_clean)

        st.markdown("## 📊 Résultat généré")
        st.markdown(output)

# ==============================================
# 10. ONGLET 2 - DOCUMENTATION
# ==============================================
with tab_doc:
    st.markdown("""
# 📘 Documentation – Paramètres IA

## 🔥 Température  
- 0.0 – 0.4 : factuel  
- 0.5 – 0.7 : neutre  
- 0.8 – 1.5 : créatif  

## 🎛 Max Tokens  
Plus élevé = réponse plus longue.

### Recommandations
| Agent | Température | Max Tokens |
|-------|-------------|------------|
| Investisseur | 0.2 – 0.5 | 2500 – 4000 |
| Presse / SEO | 0.7 – 1.2 | 1500 – 3000 |
| LinkedIn | 0.8 – 1.3 | 300 – 600 |
""")
