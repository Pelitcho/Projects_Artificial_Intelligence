import requests
from openai import OpenAI

# -------------------------------------------
# CONFIG 
# -------------------------------------------

PPLX_URL = "https://api.perplexity.ai/chat/completions"

# -------------------------------------------
# FONCTION : récupère données avec Perplexity
# -------------------------------------------
def search_perplexity(query, perplexity_key):
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": "Tu es un moteur de recherche financier."},
            {"role": "user", "content": query}
        ]
    }

    headers = {
        "Authorization": f"Bearer {perplexity_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(PPLX_URL, json=payload, headers=headers)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]

# -------------------------------------------
# FONCTION : transforme données via ChatGPT
# -------------------------------------------
def analyze_with_chatgpt(perplexity_data, topic, openai_key):
    client = OpenAI(api_key=openai_key)

    prompt = f"""
    Sujet : {topic}

    Données Perplexity :
    {perplexity_data}

    """

    chat_completion = client.chat.completions.create(
        model="gpt-5.1",
        messages=[
            {"role": "user", 
             "content": prompt
            } 
        ]
    )

    return chat_completion.choices[0].message.content

# -------------------------------------------
# PIPELINE COMPLET
# -------------------------------------------
def investor_agent(topic, perplexity_key, openai_key):

    data = search_perplexity(topic, perplexity_key)

    result = analyze_with_chatgpt(data, topic, openai_key)

    return result
