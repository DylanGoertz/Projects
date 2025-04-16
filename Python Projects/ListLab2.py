def bubble_sort( a ): # ascending order
    for k in range( len(a) ): # number of passes
        for i in range( len(a) - 1 -k):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    return a

def main():

    values = ["henry", "emma", "bill", "sophia", "benjamin", "amelia", "isabella", "gene"]

    values.sort(reverse=True)
    print("Names sorted in descending order")
    print(values)
    


main()

