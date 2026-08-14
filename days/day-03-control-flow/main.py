"""Day 03 — Control Flow — Treasure Island"""

import random


def main() -> None:
    print("Day 03 — Control Flow — Treasure Island")
    odd_or_even = int(input("Give me a number : "))

    module = odd_or_even % 2

    if module == 0:
        print("The number is Even!")
    else:
        print("The number is Odd!")


if __name__ == "__main__":
    main()
