def main():

    num = int(input("Input a number from 1-7: "))

    if 1 <= num <= 7:
        days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
        print(days[num])
    else:
        print("Error: Number must be between 1 and 7.")

main()
    
