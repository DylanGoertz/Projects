def main():

    import turtle as t
    A = eval(input("Enter side A: "))
    B = eval(input("Enter side B: "))
    C = eval(input("Enter side C: "))
    D = eval(input("Enter side D: "))
    E = eval(input("Enter side E: "))
    x1 = A * B
    F = D - (B + E)
    G = A - C
    x2 = F * G
    x3 = E * G * 0.5
    y = x1 + x2 + x3
    print("Room Area: " , y )


main()
    


