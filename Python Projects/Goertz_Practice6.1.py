def main():
    with open('my_name.txt', 'r') as file:
        lines = file.readlines()

        your_name = lines[0].strip()
        other_name = lines[1].strip()
        your_age = int(lines[2])

        age_divided_by_2 = your_age / 2

        print(f"Your Name: {AAA}")
        print(f"Someone Else's Name: {BBB}")
        print(f"Your Age: {your_age}")
        print(f"Your Age Divided by 2: {age_divided_by_2}")

main()
