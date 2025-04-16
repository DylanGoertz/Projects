def linear_search( a , item):
    for i in range( len(a) ):
        if item == a[i]:
            return i
        
    return -1

    
def main():

    values = ["Henry", "emma", "bill", "sophia", "benjamin", "amelia", "isabella", "gene"]
    found = linear_search(values, 99)
    print("There are 8 values in the list")
    print("Henry, emma, bill, sophia, benjamin, amelia, isabella, and gene")
    found = eval(input("Which name to find? "))
    if found >= 0:
        print(values[found],"is in the list")
    else:
        print("search item is not in the list")



main()
