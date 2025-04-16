import Box

def main():
    b1 = Box.box ( 45.5 , 34.5 , 14.3 )
    print(repr(b1))
    print(f"The volume of box is {b1.getVolume():.2f}")
    print(f"The surface area is {b1.getSurfaceArea():.3f}")
    


main()
