# Dylan Goertz
# Program Status: Complete
# This program has a function that accpets two arguments: a list and a number n. the user will then input
# 10 integers and then the program will display the original list as well as the list which have the numbers
# greater than n

# this funtion accepts two arguments and will be able to decide which numbers are larger than n
def display_larger(n, number_list):
    larger_numbers = []
    for num in number_list:
        if num > n:
            larger_numbers.append(num)
            
    print("Number:", n)
    print("List of numbers:")
    print(number_list)
    print("List of numbers that are larger than", n,":")
    print(larger_numbers)

# this is the main funtion that will ask for the 10 integers from the user as well as the number they
# would like to test
def main():

    print("Enter a list of 10 integers")
    number_list = []
    for i in range(10):
        num = int(input("Enter a number: "))
        number_list.append(num)
    
    n = int(input("Enter the number you wish to test if the list elements are greater than: "))
    
    display_larger(n, number_list)
    
main()
