def main():

    import turtle as t
    print("This program illustrates a chaotic funtion")
    x = eval(input("Enter a number between 0 and 1: "))
    t.penup()
    t.backward(600)
    t.pendown()
    for i in range(500):
        x = 3.9 * x * (1-x)
        y= int(360 * x)
        t.setheading( y )
        t.forward(10)
        print(x)

main()
