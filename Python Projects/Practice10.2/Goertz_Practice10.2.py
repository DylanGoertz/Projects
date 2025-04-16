import pet

def main():
    my_pet = pet.Pet()

    name = input("Enter the name of your pet: ")
    animal_type = input("Enter the type of animal: ")
    age = int(input("Enter the age of your pet: "))

    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)

    print("Pet Details:")
    print("Name:", my_pet.get_name())
    print("Animal Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())

main()
