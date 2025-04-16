# Dylan Goertz
# Program Status: Complete
# This program reads a string from the user containing a date
# in the form mm/dd/yyyy. 

# main function
def main():
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

    date_str = input('Enter a date in the format mm/dd/yyyy: ')

    month_str, day_str, year_str = date_str.split('/')

    month_num = int(month_str)

    month_name = MONTHS[month_num - 1]

    print(month_name, day_str + ',', year_str)

main()
