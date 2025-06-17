# Write a program which accepts n number from user and store it into list.return minimum number from that list.
# Input Number of elements: 4
# Input Elemments : 13 5 45 7 
# output : 5

def main():
 Size=int(input("Enter the size of the list"))
 print("enter the elements")

 Data=list()
 
 for i in range(Size):
    no=int(input())
    Data.append(no)

 Min_Num=Data[0]
 for i in Data:
      if i < Min_Num:
         Min_Num=i

 print("the Minimum Number in the list is",Min_Num)


if __name__=="__main__":
    main()
