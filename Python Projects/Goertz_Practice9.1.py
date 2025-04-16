def create_dictionary():
    emails = {}
    while True:
        print("Add entries to the email dictionary:")
        name = input("Enter a name: ")
        email = input("Enter an email address: ")
        emails[name] = email
        choice = input("Do you want to add another? (y/n): ").strip().lower()
        if choice == 'n':
            break
    return emails

def main():
    emails = create_dictionary()

    print("Name              Email Adress")
    print("------------------------------")
    print("Number of entires in email dictionary: ", len(emails))
    for name, email in emails.items():
        print(name, "       ", email)

if __name__ == '__main__':
    main()
    
        
    
