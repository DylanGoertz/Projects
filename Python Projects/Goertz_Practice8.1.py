def main():
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")

    full_name = first_name + " " + middle_name + " " + last_name

    count_a = 0
    count_e = 0
    count_s = 0

    for letter in full_name:
        if letter in 'aA':
            count_a += 1
        elif letter in 'eE':
            count_e += 1
        elif letter in 'sS':
            count_s += 1

    print("Count of 'a' or 'A' letters:", count_a)
    print("Count of 'e' or 'E' letters:", count_e)
    print("Count of 's' or 'S' letters:", count_s)

main()
