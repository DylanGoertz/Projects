class main():

    name = input("Enter name: ")
    month = int(input("Enter the month number you were born, for example, jan = 1 ,feb = 2, march = 3, etc. "))
    year = int(input("Enter the 4-digit year you were born in: "))
    
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
            

main()        
