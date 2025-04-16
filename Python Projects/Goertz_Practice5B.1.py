# This program genertaes a random floating point number between 1 and 100
# and will be used as a radius of a circle which will then calculate into the
# area of the circle

import random
import math

def get_radius():
    return random.uniform(1.0, 100.0)

def get_area(radius):
    return math.pi * radius**2

def main():
    radius = get_radius()
    area = get_area(radius)
    print("Radius of a circle is: ", radius)
    print("Area of a circle is: ", area)

main()
    
    
    
