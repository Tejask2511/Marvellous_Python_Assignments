# Write a program which accepts n number from user and store it into list.
# accept one another number from user and return frequecy of that number from the list 
#Input: number of Elements:11
#Input elements: 13 5 45 7 4 56 5 34 2 5 65 
# Elements to search: 5 
# output : 3 



def main():
    size=int(input("enter the list size"))
    print("enter the elements:")

    Data=list()
    for i in range(size):
        no=int(input())
        Data.append(no)

    frequency ={}
    for no in Data:
        if no in frequency:
            frequency[no] +=1
        else:
            frequency[no] =1

    print("frequency of each number:")
    for no,count in frequency.items():
        print(f"{no}:{count}")



if __name__=="__main__":
    main()