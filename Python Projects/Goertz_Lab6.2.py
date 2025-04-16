# Dylan Goertz
# Program Status: Complete
# This program will read random numbers from the file just made, then displays
# the data

def main():
    file=open("random_numbers_writer.txt",'r')     
    total=0        
    total_count=0   
    for line in file:   
        num=int(line)
        print(num)    
        total=total+num   
        total_count+=1         
    print("Total Of the numbers in file: ",total)   
    print("Total count of numbers in file: ",total_count)

main()
