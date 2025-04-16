def main():
    with open("number_list.txt", "w") as file:
        for num in range(50, 101):
            file.write(str(num) + "\n")

main()
