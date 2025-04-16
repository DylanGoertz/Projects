def main():

    while True:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      sum = num1 + num2
      print("The sum of", num1, "and", num2, "is", sum)
  
      choice = input("Do you want to add more numbers (y/n)? ")
      if choice != 'y':
        print("Exiting the program...")
        quit()

main()
