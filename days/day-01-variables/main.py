"""Day 01 — Variables — Band Name Generator"""


def main() -> None:

    print('Welcome to the band generator')
    city_name = input("What is the name of the city you grew up in?\n")
    pet_name = input("what is yours pet name?\n")
    
    print("Your Band name could be " + city_name + " " + pet_name)

    # def generate_band_name(name: str, last_name: str) -> str:
    #     return name + " " + last_name

    # print("Day 01 — Variables — Band Name Generator" + " " + generate_band_name(name, last_name))


if __name__ == "__main__":
    main()
