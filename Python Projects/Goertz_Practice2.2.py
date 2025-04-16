def main():

    GROSS_PAY = float(input("What is your monthly gross income? "))
    MONTHLY_DEDUCTIONS = float(input("Enter monthly paycheck deuctions: "))
    NET_MONTHLY = GROSS_PAY - MONTHLY_DEDUCTIONS
    YEARLY_GROSS_PAY = GROSS_PAY * 12
    YEARLY_NET_PAY = YEARLY_GROSS_PAY - MONTHLY_DEDUCTIONS * 12

    print("Monthly net income is: $", f'{NET_MONTHLY:,.2f}')
    print("Yearly gross pay is: $", f'{YEARLY_GROSS_PAY:,.2f}')
    print("Yearly net pay is: $", f'{YEARLY_NET_PAY:,.2f}')

main()
