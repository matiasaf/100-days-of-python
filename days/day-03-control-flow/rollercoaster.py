"""Day 03 — Control Flow — Rollercoaster."""

def main() -> None:
    print("Welcome to the rollercoaster!")

    height = int(input("What is your height in cm? "))

    if height > 120:
        print("You can ride the rollercoaster!")

        age = int(input("What is your age? "))

        if age < 12:
            ticket_price = 5
        elif age <= 18:
            ticket_price = 7
        else:
            ticket_price = 12

        if (input("do you want a photo? (y/n) ") == 'y'):
            ticket_price+=3

        print(f"Please pay ${ticket_price}.")
    else:
        print("Sorry, you have to grow taller before you can ride.")


if __name__ == "__main__":
    main()
