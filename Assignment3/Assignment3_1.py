# Write a program which accepts n number from user and store it into list.return addition of all elements from the list
# Input: number of Elements:6
# Input elements: 13 5 45 7 4 56 
# output : 130


def main():
 Size=int(input("Enter the number of Elements"))

 Data=list()

 print("Enter the Values")
 for i in range(Size):
    no=int(input())
    Data.append(no)
     
 sum=0
 for i in Data:
       sum+=i
    
 print("the Sum of list elements is",sum)


if __name__=="__main__":
    main()