import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from src.generator import generate_mission


# ============================================
# Configuration
# ============================================

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="Walk & Notice",
    page_icon="🌿",
    layout="centered",
)


# ============================================
# Header
# ============================================

st.title("🌿 Walk & Notice")

st.markdown(
    """
### AI should help you leave the screen — not keep you on it.

Choose a few preferences and get a simple outdoor observation mission.

**Generate it. Read it. Then put your phone away.**
"""
)


# ============================================
# API Configuration
# ============================================

if not OPENROUTER_API_KEY:
    st.error(
        "OPENROUTER_API_KEY is not configured. "
        "Add it to your .env file."
    )
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


# ============================================
# User Preferences
# ============================================

duration = st.selectbox(
    "⏱️ How much time do you have?",
    [15, 30],
)

environment = st.selectbox(
    "🌳 Where are you going?",
    [
        "Urban park",
        "Garden",
        "Street",
        "Neighborhood",
        "Open outdoor area",
    ],
)

interest = st.selectbox(
    "🔎 What interests you?",
    [
        "Birds",
        "Trees",
        "Sounds",
        "Nature",
        "People and surroundings",
        "Anything interesting",
    ],
)

energy = st.selectbox(
    "⚡ How are you feeling?",
    [
        "Low",
        "Medium",
        "High",
    ],
)


# ============================================
# Mission Generation
# ============================================

if st.button(
    "🌿 Generate My Mission",
    type="primary",
    use_container_width=True,
):

    with st.spinner("Creating your outdoor mission..."):

        try:
            mission = generate_mission(
                client=client,
                duration=duration,
                environment=environment,
                interest=interest,
                energy=energy,
            )

            st.session_state["mission"] = mission

        except Exception as exc:
            st.error(
                f"Could not generate a mission: {exc}"
            )


# ============================================
# Mission Display
# ============================================

if "mission" in st.session_state:

    st.divider()

    st.subheader("🌱 Your Mission")

    st.markdown(st.session_state["mission"])

    st.success(
        "Mission ready. Now put your phone away and go notice something."
    )