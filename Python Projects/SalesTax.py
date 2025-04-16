def main():
    x = eval(input("How much is the purchase price?"))
    print("Item price: ", x )
    y = 0.825
    c = x * y
    print("Sales tax: ", c )
    b = x + c
    print("Total cost: ", b )

main()
