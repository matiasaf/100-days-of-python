import secrets
import random
import string

import streamlit as st


def generate_password_easy(nr_letters: int, nr_symbols: int, nr_numbers: int) -> str:
    letters = list("abcdefghijklmnopqrstuvwxyz")
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password = ""

    for _ in range(nr_letters):
        password += random.choice(letters)

    for _ in range(nr_symbols):
        password += random.choice(symbols)

    for _ in range(nr_numbers):
        password += random.choice(numbers)

    return password


def password_generator() -> None:
    print("Welcome to the PyPassword Generator!")

    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    return generate_password_easy(nr_letters, nr_symbols, nr_numbers)


# def generate_password(letters: int, symbols: int, numbers: int) -> str:
#     characters = (
#         [secrets.choice(string.ascii_letters) for _ in range(letters)]
#         + [secrets.choice("!#$%&()*+") for _ in range(symbols)]
#         + [secrets.choice(string.digits) for _ in range(numbers)]
#     )

#     secrets.SystemRandom().shuffle(characters)
#     return "".join(characters)


st.title("🔐 Generador de contraseñas")

letters = st.slider("How many letters would you like in your password?", 1, 30, 10)
symbols = st.slider("How many symbols would you like?", 0, 15, 3)
numbers = st.slider("How many numbers would you like?", 0, 15, 3)

if st.button("Generar contraseña"):
    password = generate_password_easy(letters, symbols, numbers)
    st.code(password)
