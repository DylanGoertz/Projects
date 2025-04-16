# Dylan Goertz
# Program Status: Complete
# This program will display the needed ingredients to make a certain amount
# of servings that the user will input

def main():
    
    #Named Constants
    RECIPE_TOMATO_SAUCE = 2.00
    RECIPE_TOMATO_PASTE = 0.333
    RECIPE_CLOVES_GARLIC = 2.00
    RECIPE_TABLESPOONS_OREGANO = 1.00

    #user input for amount of servings they need
    Servings = float(input("Enter the number of servings of spaghetti sauce you want to make: "))

    #Formulas
    Tomato_Sauce_Formula = 2.00 * Servings / 4
    Tomato_Paste_Formula = 0.333 * Servings / 4
    Garlic_Cloves_Formula = 2.00 * Servings / 4
    Oregano_Tablespoons_Formula = 1.00 * Servings / 4

    #Display results
    print("To make", Servings, "servings of spaghetti sauce, you will need: ")
    print(f'{Tomato_Sauce_Formula:.2f}', "cups of tomato sauce")
    print(f'{Tomato_Paste_Formula:.2f}', "cups of tomato paste")
    print(f'{Garlic_Cloves_Formula:.2f}', "cloves of garlic")
    print(f'{Oregano_Tablespoons_Formula:.2f}', "tablespoons of oregano")

main()

    
