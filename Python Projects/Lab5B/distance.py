# This module is to calculate distance of a falling object

def falling_distance(time):
    g = 9.8
    distance = 0.5 * g * (time**2)
    return distance
