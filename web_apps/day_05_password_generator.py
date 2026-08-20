"""Day 05 — secure password generator logic and Streamlit view."""

import secrets
import string

import streamlit as st


SYMBOLS = "!#$%&()*+,-./:;=?@[]^_{|}~"


def generate_password(letters: int, symbols: int, numbers: int) -> str:
    """Generate a securely shuffled password with the requested composition."""
    counts = (letters, symbols, numbers)
    if any(count < 0 for count in counts):
        raise ValueError("Character counts cannot be negative.")
    if sum(counts) == 0:
        raise ValueError("A password must contain at least one character.")

    characters = (
        [secrets.choice(string.ascii_letters) for _ in range(letters)]
        + [secrets.choice(SYMBOLS) for _ in range(symbols)]
        + [secrets.choice(string.digits) for _ in range(numbers)]
    )
    secrets.SystemRandom().shuffle(characters)
    return "".join(characters)


def render_password_generator() -> None:
    """Render the password generator page."""
    st.markdown('<p class="eyebrow">Day 05 · Utility</p>', unsafe_allow_html=True)
    st.title("🔐 Password Generator")
    st.write("Choose a combination and generate a secure password instantly.")

    with st.container(border=True):
        letters = st.slider("Letters", min_value=1, max_value=30, value=12)
        symbols = st.slider("Symbols", min_value=0, max_value=15, value=3)
        numbers = st.slider("Numbers", min_value=0, max_value=15, value=3)

        if st.button(
            "Generate password", type="primary", use_container_width=True
        ):
            st.session_state.generated_password = generate_password(
                letters, symbols, numbers
            )

    password = st.session_state.get("generated_password")
    if password:
        st.success(f"Your {len(password)}-character password is ready.")
        st.code(password, language=None)
        st.caption("Use the copy icon in the code box to copy your password.")
