def main():
    
    name = input("Enter your first and last name or zzz to quit ")
    while name != 'zzz':
        
        month = get_month()

        year = get_year()

        season = find_season(month)

        if is_leap_year(year):
            leap_year = ' was a leap year'
        else:
            leap_year = ' was not a leap year'

        print("\nHello, ", name, "! You were born in the ", season, " and ", year, leap_year, '.', sep='')
        print()

        num_pennies = int(input("Enter number of pennies in your penny jar: "))
        penny_jar(num_pennies)

        name = input("\nEnter your first and last name or zzz to quit: ")

def get_month():
    user_month = int(input("What was the month number you were born? "))
    while user_month < 1 or user_month > 12:
        print("Must be a number between 1 and 12")
        user_month = int(input("What was the month number you were born? "))
    return user_month

def get_year():
    user_year = int(input("What year were you born in? "))
    while user_year < 0 or user_year == 0:
        print("Must be a number greater than 0")
        user_year = int(input("What year were you born in? "))
    return user_year

def find_season(user_month):
    if user_month == 12 or user_month <= 2:
        season = 'winter'
    elif user_month <= 5:
        season = 'spring'
    elif user_month <= 8:
        season = 'summer'
    else:
        season = 'fall'
    return season

def is_leap_year(user_year):

    return(user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0)

def penny_jar(pennies):
    original_pennies = pennies
    
    dollars = pennies // 100
    pennies -= dollars * 100

    quarters = pennies // 25
    pennies -= quarters * 25

    dimes = pennies // 10
    pennies -= dimes * 10

    nickels = pennies // 5
    pennies -= nickels * 5

    print(f"{original_pennies} breaks down into:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

main()

    
