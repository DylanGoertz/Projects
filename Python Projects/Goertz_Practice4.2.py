def main():

    low = int(input("Enter a low number: "))
    high = int(input("Enter a high number: "))

    print("First Loop Results:")
    for i in range(low, high+1):
        print(i, "\t", i*10)

    total = 0

    for i in range(low, high+1):
        total += i

    print("Total of numbers from", low, "to", high, "is:", total)

main()
