"""Streamlit entry point for the 100 Days of Python mini apps."""

import streamlit as st

from web_apps.day_05_password_generator import render_password_generator
from web_apps.day_07_hangman import render_hangman


st.set_page_config(
    page_title="Python Mini Apps",
    page_icon="🐍",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container { max-width: 1100px; padding-top: 2rem; }
        [data-testid="stSidebar"] { border-right: 1px solid #e5e7eb; }
        .app-hero {
            padding: 2.5rem;
            border-radius: 1.5rem;
            background: linear-gradient(135deg, #111827 0%, #312e81 100%);
            color: white;
            margin-bottom: 2rem;
        }
        .app-hero h1 { margin: 0 0 .5rem; font-size: 2.7rem; }
        .app-hero p { margin: 0; color: #dbeafe; font-size: 1.1rem; }
        .word-display {
            font-family: monospace;
            font-size: clamp(1.8rem, 6vw, 3.5rem);
            font-weight: 700;
            letter-spacing: .45rem;
            text-align: center;
            padding: 1.5rem;
            border-radius: 1rem;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
        }
        .eyebrow { color: #6366f1; font-weight: 700; text-transform: uppercase; }
    </style>
    """,
    unsafe_allow_html=True,
)


def go_to(page: str) -> None:
    """Navigate to one of the mini apps."""
    st.session_state.current_page = page


def render_home() -> None:
    """Render the application launcher."""
    st.markdown(
        """
        <section class="app-hero">
            <p>100 DAYS OF PYTHON</p>
            <h1>Python Mini Apps</h1>
            <p>Choose an app, play around, and see Python in action.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    password_column, hangman_column = st.columns(2, gap="large")

    with password_column:
        with st.container(border=True):
            st.caption("DAY 05 · LOOPS")
            st.subheader("🔐 Password Generator")
            st.write(
                "Create a strong password with your preferred mix of letters, "
                "numbers, and symbols."
            )
            st.button(
                "Open Password Generator",
                type="primary",
                use_container_width=True,
                on_click=go_to,
                args=("Password Generator",),
            )

    with hangman_column:
        with st.container(border=True):
            st.caption("DAY 07 · HANGMAN")
            st.subheader("🎯 Hangman")
            st.write(
                "Guess the hidden word one letter at a time before you run out "
                "of lives."
            )
            st.button(
                "Play Hangman",
                type="primary",
                use_container_width=True,
                on_click=go_to,
                args=("Hangman",),
            )


PAGES = {
    "Home": render_home,
    "Password Generator": render_password_generator,
    "Hangman": render_hangman,
}

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

with st.sidebar:
    st.title("🐍 Mini Apps")
    st.caption("Built while learning Python")
    st.divider()
    st.radio(
        "Navigation",
        options=list(PAGES),
        key="current_page",
        label_visibility="collapsed",
    )

PAGES[st.session_state.current_page]()
