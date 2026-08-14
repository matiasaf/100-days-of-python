"""Day 05 — Loops"""

import random


def find_max_score(student_scores: list[int]) -> int:
    max_score = 0

    for student in student_scores:
        if student > max_score:
            max_score = student

    return max_score


def calculate_sum(n: int) -> int:
    total_sum = 0

    for number in range(n + 1):
        total_sum += number

    return total_sum


def calculate_sum_formula(n: int) -> int:
    return int((n / 2) * (n + 1))


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

    password = generate_password_easy(nr_letters, nr_symbols, nr_numbers)
    print(f"Your password is: {password}")


def main() -> None:
    student_scores = [66, 78, 44, 91, 77]
    print(find_max_score(student_scores))

    """Gauss Challenge"""

    n = 100
    print(calculate_sum(n))
    print(calculate_sum_formula(n))

    password_generator()


if __name__ == "__main__":
    main()
