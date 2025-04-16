def main():

    month = int(input("Enter a month numerically (1-12): "))
    day = int(input("Enter a day numerically (1-31): "))
    year = int(input("Enter a year in two-digit form (00-99): "))

    MagicYear = month * day

    if MagicYear == year:
        print("That is a magic date!")
    else:
        print("This is not a magic date.")

main()
