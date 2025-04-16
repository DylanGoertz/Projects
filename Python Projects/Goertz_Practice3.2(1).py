def main():

    day = int(input("Input a number from 1-7: "))

    if day == 1:
        print('Monday')
    elif day == 2:
        print('Tuesday')
    elif day == 3:
        print('Wednesday')
    elif day == 4:
        print('Thursday')
    elif day == 5:
        print('Friday')
    elif day == 6:
        print('Saturday')
    elif day == 7:
        print('Sunday')
    else:
        print('Error: Please enter a number in the range 1-7.')

    choice = input("Do you want to continue (y/n)? ")
    if choice != 'y':
        print("Exiting the program...")

main()
