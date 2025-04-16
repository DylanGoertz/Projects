import Sphere as sph

def main():

    c = []

    values = 0.5
    while values < 20.0:
        c.append ( sph.sphere(values) )
        values += 1.0

    print("radius       volume      surface area")
    print("-------------------------------------")
    for i in range (len(c) ):
        print(f" {i:<4d}{repr(c[i]):<9s}{c[i].getVolume():<9.2f}{c[i].getSurfaceArea():<13.3f}")


main()
