# Dylan Goertz
# Program Status: Complete
# This program will write a series of random numbers to a file and each random
# number will be range of 1 through 500, then the program will let the user
# Specify how many numbers the file will hold

import random

# main function
def main():
    print("Random Number File Generator")
    count = int(input("How many random numbers should file hold: "))
    outfile = open('random_numbers_writer.txt', 'w')
    while count != 0:
        num = random.randint(1, 500)
        outfile.write(str(num) + "\n")
        count -= 1
    outfile.close()

main()
