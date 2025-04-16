# Dylan Goertz
# Program Status: Complete
# This program will ask the user how many packages they want and the program
# will determine if the user receives a discount and will then display the discount amount
# and then the total amount

def main():

    # Asking user for the quantity
    Quantity = float(input("Enter the number of packages purchased: "))

    # Price per package times amount the user wants
    Packages = 149.00 * Quantity

    # Discount formulas
    DISCOUNT_10 = Packages * 0.10
    DISCOUNT_20 = Packages * 0.20
    DISCOUNT_30 = Packages * 0.30
    DISCOUNT_40 = Packages * 0.40

    # Total cost formulas
    TOTAL_10 = Packages - DISCOUNT_10
    TOTAL_20 = Packages - DISCOUNT_20 
    TOTAL_30 = Packages - DISCOUNT_30 
    TOTAL_40 = Packages - DISCOUNT_40 


    # Using if-elif statements to check if the user get discounts or not
    if Quantity >= 10 and Quantity <= 49:
        print("Discount Amount: $", f'{DISCOUNT_10:,.2f}')
        print("Total Amount: $", f'{TOTAL_10:,.2F}')

    elif Quantity >= 50 and Quantity <= 99:
        print("Discount Amount: $", f'{DISCOUNT_20:,.2f}')
        print("Total Amount: $", f'{TOTAL_20:,.2F}')


    elif Quantity >= 100 and Quantity <= 149:
        print("Discount Amount: $", f'{DISCOUNT_30:,.2f}')
        print("Total Amount: $", f'{TOTAL_30:,.2F}')


    elif Quantity > 149:
        print("Discount Amount: $", f'{DISCOUNT_40:,.2f}')
        print("Total Amount: $", f'{TOTAL_40:,.2F}')

        
main()
