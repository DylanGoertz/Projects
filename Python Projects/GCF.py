def main():

    a = eval(input("Enter first number: "))
    b = eval(input("Enter second number: "))

    if a > b:
        small = a
    else:
        small = b
        
    i = 1

    i <= small
        
    for i in range(1, small + 1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
 
    print("The gcf of " , a , "and " , b ,"is : ", gcd )

main()
