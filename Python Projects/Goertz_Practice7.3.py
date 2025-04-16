def total_list(l):
    total = 0
    for num in l: total += num
    return total

def main():
    l1 = [1, 3, 5, 7, 9]
    l2 = [2, 4, 6, 8, 10]
    together = l1 + l2
    together.sort()
    total = total_list(together)
    print("List:", together)
    print('Total:', total)
    print('Maximum value:', max(together))
    print('Minimum value:', min(together))

main()
