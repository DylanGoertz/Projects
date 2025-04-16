def main():
    myfile = open("students.txt","r")
    next_line = myfile.readline()
    print('Name Score')
    print('---------------------')
    while next_line != "":
        print(next_line)
        next_line = myfile.readline()

main()
