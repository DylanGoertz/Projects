def main():
    with open("number_list.txt", "r") as file:
        for line in file:
            num = int(line.strip())
            print(num)

main()
