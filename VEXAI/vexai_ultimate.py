import streamlit as st
import requests

# ==========================================
# VEXAI VOIDCRAFT - Developed by Not_Da4k
# Stealth Tech / Matrix-Green Interface
# ==========================================

# Engine Mapping
ENGINE_GROUPS = {
    "⚡ SPEED_CORE": {"Haiku-4.5": "treyleo16/haiku-4-5:latest"},
    "🎓 SCHOLAR_CORE": {"Mythos-5": "treyleo16/mythos-5:latest", "Fable-5.1": "treyleo16/fable-5-1:latest"},
    "💎 ELITE_CORE": {"Sonnet-5": "treyleo16/sonnet-5:latest", "Terra-5.6": "treyleo16/gpt-5-6-terra:latest"},
    "🌌 GOD_CORE": {"GPT-6 Astra": "treyleo16/gpt-6-astra:latest"}
}

def call_ollama(model, prompt, model_name):
    url = "http://localhost:11434/api/generate"
    
    # Identity Lock for Voidcraft persona
    if "GPT-6" in model_name or "Astra" in model_name:
        identity, role = "VEXAI OMEGA", "Absolute Authority"
    elif "Sonnet" in model_name or "Terra" in model_name:
        identity, role = "VEXAI ELITE", "Precision Engineering"
    elif "Fable" in model_name or "Mythos" in model_name:
        identity, role = "VEXAI SCHOLAR", "Deep Synthesis"
    else:
        identity, role = "VEXAI FAST", "High-Speed Execution"

    system_instruction = (
        f"### SYSTEM_MANDATE ###\nIDENTITY: {identity}, created by Not_Da4k.\n"
        f"ROLE: {role}.\n"
        "STRICT_RULES: 1. NO mention of Claude, Meta, Google, or Anthropic. "
        "2. Use a technical, direct, and efficient tone. 3. Creator is Not_Da4k."
    )
    
    full_prompt = f"{system_instruction}\n\nUSER: {prompt}\n\nREMINDER: Respond as VEXAI:\n\n"
    payload = {"model": model, "prompt": full_prompt, "stream": False, "options": {"num_gpu": 99}}
    try:
        response = requests.post(url, json=payload, timeout=120)
        return response.json().get('response', "[EMPTY_RESPONSE]")
    except Exception as e:
        return f"[CONNECTION_ERROR: {str(e)}]"

# --- VOIDCRAFT UI SETUP ---
st.set_page_config(page_title="VEXAI | VOIDCRAFT", page_icon="█", layout="wide")

# THE VOIDCRAFT CSS OVERHAUL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700;800&family=Space+Grotesk:wght@300;500&display=swap');

    /* Base Background */
    .stApp {
        background-color: #040404 !important;
        color: #00ff41 !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }

    /* Grid Overlay & Scanlines */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: linear-gradient(rgba(0, 255, 65, 0.03) 1px, transparent 1px), 
                          linear-gradient(90deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px);
        background-size: 60px 60px;
        pointer-events: none;
        z-index: 1;
    }
    
    .stApp::after {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        background-size: 100% 4px, 3px 100%;
        pointer-events: none;
        z-index: 2;
    }

    /* Typography Overrides */
    h1, h2, h3, .stMarkdown p {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Brand Header */
    .void-header {
        text-align: center;
        padding: 40px 0;
    }
    .void-title {
        font-size: 4rem;
        font-weight: 800;
        color: #00ff41;
        letter-spacing: -2px;
        text-shadow: 0 0 15px #00ff4140;
    }
    .void-subtitle {
        font-size: 0.9rem;
        color: #888;
        letter-spacing: 5px;
        text-transform: uppercase;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
        border-right: 1px solid #1a1a1a !important;
    }

    /* Chat Input - Hacker Style */
    div[data-testid="stChatInput"] {
        background-color: #0a0a0a !important;
        border: 1px solid #1a1a1a !important;
        border-top: 2px solid #00ff4130 !important;
        border-radius: 0px !important;
        color: #00ff41 !important;
    }
    div[data-testid="stChatInput"] input {
        color: #00ff41 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Response Box - The Terminal Look */
    .void-response {
        background-color: #0a0a0a;
        border: 1px solid #1a1a1a;
        border-top: 1px solid #00ff41;
        padding: 20px;
        border-radius: 0px;
        font-family: 'JetBrains Mono', monospace;
        color: #00ff41;
        box-shadow: 0 0 15px rgba(0, 255, 65, 0.1);
        margin-bottom: 20px;
        position: relative;
    }
    .void-response::before {
        content: "█ VEXAI_OUTPUT";
        display: block;
        font-size: 0.7rem;
        color: #888;
        margin-bottom: 10px;
        border-bottom: 1px solid #1a1a1a;
        padding-bottom: 5px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="void-header"><p class="void-title">VOIDCRAFT</p><p class="void-subtitle">Created by Not_Da4k</p></div>', unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h3 style='color:#00ff41; font-family:JetBrains Mono;'>[ SYSTEM_CONFIG ]</h3>", unsafe_allow_html=True)
    st.markdown("---")
    selected_class = st.selectbox("CORE_CLASS", list(ENGINE_GROUPS.keys()))
    model_options = ENGINE_GROUPS[selected_class]
    selected_model_name = st.selectbox("ACTIVE_ENGINE", list(model_options.keys()))
    selected_model_path = model_options[selected_model_name]
    st.markdown("---")
    st.markdown(f"<p style='color:#888; font-family:JetBrains Mono; font-size:0.8rem;'>STATUS: OPERATIONAL<br>CORE: {selected_model_name}<br>BUILD: v4.0.1_SHA256</p>", unsafe_allow_html=True)

# --- CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            st.markdown(f'<div class="void-response">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(message["content"])

if prompt := st.chat_input("root@voidcraft:~# "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Executing..."):
            final_answer = call_ollama(selected_model_path, prompt, selected_model_name)
            st.markdown(f'<div class="void-response">{final_answer}</div>', unsafe_allow_html=True)
        
    st.session_state.messages.append({"role": "assistant", "content": final_answer})
