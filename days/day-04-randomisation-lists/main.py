"""Day 04 — Randomisation & Lists — Rock Paper Scissors"""

import random


def main() -> None:
    print("Day 04 — Randomisation & Lists — Rock Paper Scissors")
    heads_or_tail = random.random()

    if heads_or_tail <= 0.5:
        print("Heads!")
    else:
        print("Tails!")


if __name__ == "__main__":
    main()
