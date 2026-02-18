import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="Gyana | AI & Full-Stack Developer", page_icon="🚀", layout="wide")

# --- CUSTOM CSS (DARK NEON THEME) ---
st.markdown("""
    <style>
    .stApp {
        background: #0e1117;
        color: #ffffff;
    }
    .main-header {
        font-size: 50px;
        font-weight: 800;
        background: -webkit-linear-gradient(#00f2ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .profile-img {
        border-radius: 50%;
        border: 5px solid #00f2ff;
        box-shadow: 0 0 20px #00f2ff;
        transition: 0.5s;
    }
    .profile-img:hover {
        transform: scale(1.05);
        box-shadow: 0 0 40px #00f2ff;
    }
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #00f2ff;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["About Me", "Skills", "Projects", "Contact"],
        icons=["person", "code-slash", "briefcase", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#0e1117"},
            "icon": {"color": "#00f2ff", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "#0072ff"},
        }
    )

# --- HOME / ABOUT ME ---
if selected == "About Me":
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        # ఇక్కడ మీ ఫోటో ఫైల్ నేమ్ ఇవ్వండి (ఉదా: my_photo.jpg)
        st.image("image_e5496b.jpg", width=300) 
        
    with col2:
        st.markdown('<h1 class="main-header">Hi, I\'m Gyana</h1>', unsafe_allow_html=True)
        st.subheader("AI & Full-Stack Developer")
        st.write("""
            I build scalable software, solve real problems, and turn ideas into working systems.
            Expertise in **Java, DSA, AI, and Full-Stack Development**.
        """)
        if st.button("🚀 View My Projects"):
            st.balloons()

# --- SKILLS ---
elif selected == "Skills":
    st.title("🛠️ Technical Arsenal")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Languages")
        st.code("Java\nPython\nJavaScript\nSQL")
    with col2:
        st.markdown("### Frameworks")
        st.code("Streamlit\nFlask\nReact\nSpring Boot")
    with col3:
        st.markdown("### Specialized")
        st.code("NLP (SonicMind)\nFull-Stack Dev\nAPI Integration")

# --- PROJECTS ---
elif selected == "Projects":
    st.title("📂 Featured Creations")
    
    # Project 1
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3>🎙️ SonicMind AI</h3>
            <p>A voice-enabled intelligent interface that processes vocal commands and provides real-time AI responses.</p>
            <b>Tech:</b> Streamlit, Speech-to-Text, NLP
        </div>
        """, unsafe_allow_html=True)
    
    # Project 2
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3>🧠 LingoLens NLP</h3>
            <p>An advanced text analysis engine for spam detection and sentiment analysis using Naive Bayes.</p>
            <b>Tech:</b> Python, Scikit-learn, TF-IDF
        </div>
        """, unsafe_allow_html=True)

# --- CONTACT ---
elif selected == "Contact":
    st.title("📩 Get In Touch")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Signal")
        if submit:
            st.success("Signal Received! I will get back to you soon.")

st.markdown("---")
st.caption("© 2026 Gyana | Built with ❤️ using Python & Streamlit")
