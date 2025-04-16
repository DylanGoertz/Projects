def main():
    names = []
    birthdates = []

    contact_file = open("names.txt.rtf", 'r')

    name = contact_file.readline()
    while name != "":
        name = name.rstrip('\n')
        birthdate = contact_file.readline().rstrip('\n')
        names.append(name)
        birthdates.append(birthdate)

        name = contact_file.readline()

    contact_file.close()

    display_contacts(names, birthdates)

def display_contacts(contact_names, contact_birthdates):

    print(f"Name                      Age      Season       Leap Year")

    for i in range(len(contact_names)):
        age = get_age(contact_birthdates[i])
        season = find_season(contact_birthdates[i])
        if is_leap_year(contact_birthdates[i]):
            leap_year = 'yes'
        else:
            leap_year = 'no'
        print(f"{contact_names[i]:25} {age} {season} {leap_year}")

def get_age(birthdate):
    return 99


def find_season(birthdate):
    birthdate_list = birthdate.split('/')
    month = int(birthdate_list[0])
    
    if month == 12 or user_month <= 2:
        season = 'winter'
    elif month <= 5:
        season = 'spring'
    elif month <= 8:
        season = 'summer'
    else:
        season = 'fall'
        
    return season

def is_leap_year(birthdate):
    birthdate_list = birthdate.split('/')
    year = int(birthdate_list[2])
    return(user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0)


main()
