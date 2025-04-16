import random

# generates 7 random numbers and puts them in a list and then displays it
def generate_lottery_number():
    lottery_numbers = []

    for i in range(7):
        random_number = random.randint(0, 9)
        
        lottery_numbers.append(random_number)

    print("Lottery Numbers:")
    for number in lottery_numbers:
        print(number, end=' ')  
    print() 

    lottery_number_str = ''.join(map(str, lottery_numbers))
    print("Lottery Number as a String:", lottery_number_str)

    return lottery_number_str

# this function is used to let the user decide if they want to play again or not
def play_lottery():
    while True:
        lottery_number = generate_lottery_number()
        play_again = input("Do you want to play again? (yes or no): ").strip().lower()
        if play_again != "yes":
            break

play_lottery()
