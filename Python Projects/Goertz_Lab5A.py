# Dylan Goertz
# Program Status: Complete
# This program takes two functions to calculate the number of stars a resturant gets
# based on the 5 numeric scores inputed by the judges

# this function will determine the number of stars from the given average score
def get_stars(average_score):
    if average_score >= 9:
        return "*****"
    elif average_score <= 8.9 and average_score >= 8:
        return "****"
    elif average_score <= 7.9 and average_score >= 7:
        return "***"
    elif average_score <= 6.9 and average_score >= 6:
        return "**"
    elif average_score <= 5.9 and average_score >= 5:
        return "*"
    else:
        return "No stars"

# This function is the main function that ties everything together
def main():
    # initalizing these variables to use in the loops
    count = 0
    average = 0

    while count < 5:
        score = int(input("Enter critics score between 0 and 10: "))

        while score < 0 or score > 10:
            score = int(input("Error: Enter critics score between 0 and 10: "))

        average += score
        count += 1

    average /= 5

    print(f"Your score of {average:.2f} gives you {get_stars(average)}")

main()
    
