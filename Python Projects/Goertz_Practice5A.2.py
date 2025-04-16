#This program converts kilometers given by the user to miles

# Global Constant
CONVERSION_FACTOR = 0.6214

def get_miles(kilometers):

    print("The number of miles is", (kilometers * CONVERSION_FACTOR))

def main():

    kilometers = float(input("Give a distance in kilometers: "))
    get_miles(kilometers)


main()
