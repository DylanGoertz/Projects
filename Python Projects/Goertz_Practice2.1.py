#

def main():

    Burger = float(input("What is the price of a Hamburger? "))
    Fry = float(input("What is the price of fries? "))
    Shake = float(input("What is the price of a Shake? "))

    Cost = Burger + Fry + Shake
    AverageCost = Cost / 3

    print("The total cost is: $", Cost)
    print("The avergae cost is: $", AverageCost)

main()
