def main():
    import math

    pi = 3.14
    r = pi/180

    h = eval(input("Enter height ,"))
    a = eval(input(" angle "))
    l = h/math.sin(r * a)
    print("The ladder should be " , l , "in length")

main()
