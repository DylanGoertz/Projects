import pickle

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

def save(emails):
    outfile = open('myfile.dat', 'wb')
    pickle.dump(emails, outfile)
    outfile.close()

def load():
    infile = open('myfile.dat', 'rb')
    emails = pickle.load(infile)
    infile.close()
    return emails

def main():
    load_choice = input("Do you want to restore a previous version (y/n): ")
    if load_choice == 'y':
        emails = load()
    else:
        emails = create_dictionary()
        outfile = save(emails)
        print("Dictionary Saved")
    print("Number of entires in email dictionary: ", len(emails))
    print("Name              Email Adress")
    print("------------------------------")
    for name, email in emails.items():
        print(name, "            ", email)

if __name__ == '__main__':
    main()
