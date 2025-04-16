def main():

    n=int(input("Enter a whole number:"))
    print("Divisors:")
    for i in range(1,n+1):
        if(n%i==0):
            print(i)

main()
        
