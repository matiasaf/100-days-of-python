import secrets
import random
import string

import streamlit as st


def generate_password_easy(nr_letters: int, nr_symbols: int, nr_numbers: int) -> str:
    letters = list("abcdefghijklmnopqrstuvwxyz")
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = []
    final_password = ""

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # Mix the characters into a random order.
    random.shuffle(password_list)

    # Concatenate all characters into the final password string.
    for item in password_list:
        final_password += item

    return final_password


def generate_password(letters: int, symbols: int, numbers: int) -> str:
    # secrets is used here to generate characters securely.
    characters = (
        [secrets.choice(string.ascii_letters) for _ in range(letters)]
        + [secrets.choice("!#$%&()*+") for _ in range(symbols)]
        + [secrets.choice(string.digits) for _ in range(numbers)]
    )

    secrets.SystemRandom().shuffle(characters)
    return "".join(characters)


st.title("🔐 Welcome to the PyPassword Generator!")

letters = st.slider("How many letters would you like in your password?", 1, 30, 10)
symbols = st.slider("How many symbols would you like?", 0, 15, 3)
numbers = st.slider("How many numbers would you like?", 0, 15, 3)

if st.button("Generate password"):
    password = generate_password_easy(letters, symbols, numbers)
    st.code(password)
