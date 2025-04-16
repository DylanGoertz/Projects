# This program will calculate the area of a square based on a randomly
# generated interger to be used as the side

import random
import square

def main():
    side = random.randint(1, 100)
    print("The area of the square is", square.area(side))
    print("The perimeter of the squaree is", square.perimeter(side))

main()
    
