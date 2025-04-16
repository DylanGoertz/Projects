def main():

    budget = float(input("Enter amount budgeted for the month: "))

    total_expenses = 0.0

    while True:
        expense = float(input("Enter an amount spent (0 to quit): "))

        if expense == 0:
            break

        total_expenses += expense

    difference = budget - total_expenses
    
    print("Budgeted: $", budget)
    print("Spent: $", total_expenses)

    if difference > 0:
        print("You are under budget by $", difference)

    elif difference < 0:
        print("You are over budget by $", abs(difference))

    else:
        print("You have spent exactly your budget.")

main()
