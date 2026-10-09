import streamlit as st
from dotenv import load_dotenv

from src.generator import generate_mission


load_dotenv()


st.set_page_config(
    page_title="Walk & Notice",
    page_icon="🌿",
    layout="centered",
)


st.title("🌿 Walk & Notice")

st.markdown(
    """
### AI should help you leave the screen — not keep you on it.

Choose a few preferences and get a simple outdoor observation mission.

**Generate it. Read it. Then put your phone away.**
"""
)


st.subheader("🤖 Choose AI Provider")

provider_label = st.radio(
    "How should the mission be generated?",
    [
        "🦙 Local Gemma 4 E4B — Ollama",
        "☁️ OpenRouter",
    ],
)


if provider_label.startswith("🦙"):
    provider = "ollama"

    st.info(
        "Running locally: Gemma 4 E4B → Ollama → your RTX 3060."
    )

else:
    provider = "openrouter"

    st.info(
        "Running through OpenRouter using the configured open-weight model."
    )


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


if st.button(
    "🌿 Generate My Mission",
    type="primary",
    use_container_width=True,
):

    with st.spinner(
        f"Generating mission using {provider}..."
    ):

        try:

            mission = generate_mission(
                duration=duration,
                environment=environment,
                interest=interest,
                energy=energy,
                provider=provider,
            )

            st.session_state["mission"] = mission
            st.session_state["provider"] = provider

        except Exception as exc:

            st.error(
                f"Could not generate a mission: {exc}"
            )


if "mission" in st.session_state:

    st.divider()

    provider_used = st.session_state.get(
        "provider",
        "unknown",
    )

    if provider_used == "ollama":
        st.caption(
            "🦙 Generated locally with Gemma 4 E4B via Ollama."
        )
    else:
        st.caption(
            "☁️ Generated through OpenRouter."
        )

    st.subheader("🌱 Your Mission")

    st.markdown(
        st.session_state["mission"]
    )

    st.success(
        "Mission ready. Now put your phone away "
        "and go notice something."
    )