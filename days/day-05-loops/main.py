"""Day 05 — Loops"""


def main() -> None:
    student_scores = [66, 78, 44, 91, 77]
    max_score = 0

    for student in student_scores:
        if student > max_score:
            max_score = student

    print(max_score)


if __name__ == "__main__":
    main()
