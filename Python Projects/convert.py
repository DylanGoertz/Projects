#convert.py
# A program to convert Celsius to Farenheit
#by: Susan Computewell

def main():
    for i in range(5):
        celcius = eval(input("What is the celsius temperature? "))
        fahernheit = 9/5 * celcius + 32
        print("The temerature is", fahernheit, "degrees Fahrenheit.")
   

main()
