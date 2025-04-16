# Dylan Goertz
# Program Status: Complete
# This program will calculate the distance in meters based on the objects
# falling distance

import distance

# main function that will call upon distance.py
def main():

    print("Time    Falling Distance")
    print("")
    print("------------------------")
    print("")

    for time in range(1,11):
        distance_meters = distance.falling_distance(time)
        print(f"{time:2}      {distance_meters:.2f}")



main()
