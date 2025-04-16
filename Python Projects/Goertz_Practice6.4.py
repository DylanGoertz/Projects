def main():
    try:
        with open("number_list.txt", "r") as file:
            total_sum = 0
            count = 0
        
            for line in file:
                try:
                    number = float(line)
                    total_sum += number
                    count += 1
                except ValueError:
                    print(f"Warning: Skipping line '{line.strip()}' as it's not a valid number.")
        
            if count > 0:
                average = total_sum / count
            else:
                average = 0

            print(f"Sum: {total_sum}")
            print(f"Average: {average}")

    except IOError:
        print("Error: Unable to open the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
