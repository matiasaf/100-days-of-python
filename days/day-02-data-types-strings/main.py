"""Day 02 — Data Types & Strings — Tip Calculator"""


def main() -> None:
    print("Day 02 — Data Types & Strings — Tip Calculator")

    # print("Hello"[3])
    # print(type("Matias"))
    # print(type(111_999))
    # print(type(1.3))150
    # print(type(False))
    print('Welcome to the tip calculator!')
    total_bill =  float(input("What was the total bill? "))
    tip = int(input("How much tip would you like to give? 10, 12, or 15 ? "))
    people_count = int(input("How many people to split the bill? "))

    total_bill_with_tip_percentage = total_bill + (total_bill * tip / 100);
    total_bill_per_person = round(total_bill_with_tip_percentage / people_count, 2)

    print(f"Each person sould pay: ${total_bill_per_person}")

if __name__ == "__main__":
    main()
