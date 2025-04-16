def main():

    matrix = [[0] * 3 for _ in range(4)]

    for row in range(4):
        for col in range(3):
            value = int(input(f"Enter an integer for element at row {row + 1}, column {col + 1}: "))
            matrix[row][col] = value

    total = 0

    for row in range(4):
        for col in range(3):
            value = matrix[row][col]
            total += value
            print(f"Element at row {row + 1}, column {col + 1}: {value}")

    print(f"Total sum of all elements: {total}")

main()
