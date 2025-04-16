def main():
    
    name = input("Enter your first and last name or zzz to quit ")
    while name != 'zzz':
        
        month = int(input("What was the month number you were born? "))
        while month < 1 or month > 12:
            print("Must be a number between 1 and 12")
            month = int(input("What was the month number you were born? "))

        year = int(input("What year were you born in? "))
        while year < 0 or year == 0:
            print("Must be a number greater than 0")
            year = int(input("What year were you born in? "))

        if month == 12 or month == 1 or month == 2:
            season = 'winter'
        elif month <= 5:
            season = 'spring'
        elif month <= 8:
            season = 'summer'
        else:
            season = 'fall'

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = 'was a leap year'
                else:
                    leap = 'was not a leap year'
            else:
                leap = 'was a leap year'
        else:
            leap = 'was not a leap year'

        print(f"Hello, {name}! You were born in the {season} and {year} {leap}.")

        name = input("Enter your first and last name or zzz to quit ")


main()
