import streamlit as st
import os
import time
from streamlit_option_menu import option_menu
from streamlit_mic_recorder import mic_recorder

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Veerababu | SonicMind AI", 
    page_icon="🛡️", 
    layout="wide"
)

# --- 2. PREMIUM DARK NEON CSS ---
st.markdown("""
    <style>
    .stApp { background: #000b1a; color: #00d4ff; }
    .main-header {
        font-size: 60px; font-weight: 800;
        background: -webkit-linear-gradient(#00d4ff, #0055ff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .project-card {
        background: rgba(0, 212, 255, 0.05);
        padding: 25px; border-radius: 15px;
        border-left: 5px solid #00d4ff; margin-bottom: 20px;
        transition: 0.3s;
    }
    .project-card:hover { transform: translateY(-5px); background: rgba(0, 212, 255, 0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- 4. LOGIN SYSTEM ---
if not st.session_state.authenticated:
    _, col2, _ = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<br><br><h1 style='text-align:center;'>VeeRA Gateway</h1>", unsafe_allow_html=True)
        u_id = st.text_input("CREATOR IDENTITY", placeholder="Learnomine_Creator")
        u_key = st.text_input("NEURAL KEY", type="password", placeholder="CHAT_AI_2026")
        if st.button("ACTIVATE SYSTEM"):
            if u_id == "Learnomine_Creator" and u_key == "CHAT_AI_2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid Credentials")
    st.stop()

# --- 5. NAVIGATION ---
with st.sidebar:
    selected = option_menu(
        "VeeraSync AI", ["About Me", "SonicMind AI", "LingoLens NLP", "Contact"],
        icons=['person-badge', 'mic', 'brain', 'envelope'], 
        menu_icon="cpu", default_index=0,
        styles={"nav-link-selected": {"background-color": "#0055ff"}}
    )
    if st.button("Shutdown Session"):
        st.session_state.authenticated = False
        st.rerun()

# --- 6. SECTIONS ---
if selected == "About Me":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        # IMAGE ERROR FIX: Check if file exists
        img_path = "image_e5496b.jpg"
        if os.path.exists(img_path):
            st.image(img_path, width=350)
        else:
            # Placeholder image if file is missing in GitHub
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=300)
            st.warning("⚠️ Photo 'image_e5496b.jpg' not found in repo. Upload it to GitHub to fix this.")
            
    with col2:
        st.markdown(f'<h1 class="main-header">Veerababu</h1>', unsafe_allow_html=True)
        st.subheader("AI Architect & NLP Developer")
        st.write("Innovative creator of **SonicMind** and **VeeRA Intelligence** systems. Expert in turning complex neural concepts into interactive user experiences.")
        st.info("🚀 Specialization: Voice-AI Sync & Asynchronous Text Analysis.")

elif selected == "SonicMind AI":
    st.title("🎙️ SonicMind Voice Interface")
    st.write("Speak to the neural engine and watch it process in real-time.")
    
    col_v, col_c = st.columns([1, 2])
    with col_v:
        audio = mic_recorder(start_prompt="🎤 Start Listening", stop_prompt="🛑 Process Voice", key='sonic')
    with col_c:
        if audio:
            with st.status("Decoding Audio Signal..."):
                time.sleep(1)
                st.success("SonicMind: I have received your vocal command, Veerababu!")
        else:
            st.chat_input("Or type your command...")

elif selected == "LingoLens NLP":
    st.title("🧠 LingoLens Analysis Engine")
    text_in = st.text_area("Enter text for neural classification:")
    if st.button("Run Inference"):
        with st.spinner("Analyzing TF-IDF Vectors..."):
            time.sleep(1)
            st.success("Classification: LEGITIMATE MESSAGE ✅")

elif selected == "Contact":
    st.title("📩 Neural Contact Point")
    st.text_input("Your Name")
    st.text_area("Message")
    st.button("Send Signal")

st.markdown("---")
st.caption("VeeraSync AI V2.0 | Built by Veerababu | 2026")
