import secrets
import string

import streamlit as st


def generate_password(letters: int, symbols: int, numbers: int) -> str:
    characters = (
        [secrets.choice(string.ascii_letters) for _ in range(letters)]
        + [secrets.choice("!#$%&()*+") for _ in range(symbols)]
        + [secrets.choice(string.digits) for _ in range(numbers)]
    )

    secrets.SystemRandom().shuffle(characters)
    return "".join(characters)


st.title("🔐 Generador de contraseñas")

letters = st.slider("Cantidad de letras", 1, 30, 10)
symbols = st.slider("Cantidad de símbolos", 0, 15, 3)
numbers = st.slider("Cantidad de números", 0, 15, 3)

if st.button("Generar contraseña"):
    password = generate_password(letters, symbols, numbers)
    st.code(password)
