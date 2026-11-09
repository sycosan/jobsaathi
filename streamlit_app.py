"""
JobSaathi Intelligence - Streamlit host for the interactive BI dashboard.
The dashboard itself is index.html (same repository); this file serves it inside Streamlit.
SYNTHETIC DEMONSTRATION DATA - 5,000 respondents, not real customers.
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="JobSaathi Intelligence", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

# remove Streamlit's default padding/header so the dashboard uses the full window
st.markdown("""
<style>
  .block-container {padding: 0 !important; max-width: 100% !important;}
  header[data-testid="stHeader"], footer, #MainMenu {display: none !important;}
  iframe {border: 0; display: block;}
</style>
""", unsafe_allow_html=True)

html_file = Path(__file__).parent / "index.html"
if not html_file.exists():
    st.error("index.html was not found next to streamlit_app.py. Upload index.html to the same folder of the repository.")
    st.stop()

components.html(html_file.read_text(encoding="utf-8"), height=1400, scrolling=True)
