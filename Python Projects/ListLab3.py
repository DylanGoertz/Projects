def bubble_sort( list ): 
    for k in range( len(list) ): 
        for i in range( len(list) - 1 -k):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

def binary_search(list, item):

    first=0
    last=len(list)-1
    while(first<=last):
        middle=(first+last)//2
        if item==list[middle]:
            return middle
        if item < list[middle]:
            last = middle-1
        if item > list[middle]:
            first = middle+1
    return-1

def main():

    list = [13, 2, 19, 9, 34, 5, 24, 12, 3, 21, 7, 18, 44]

    print("list sorted")
    print(bubble_sort(list) )
    print("Ready for searching with binary search")
    y = eval(input("Enter a search value: ") )
    index = binary_search(list, y)
    if index>=0:
        print(y, "is at index position: ", index)
    if index<0:
        print("The value", y, "is not in the list")


main()

   
