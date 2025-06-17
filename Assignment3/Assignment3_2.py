# Write a program which accepts n number from user and store it into list.return maximum number from that list.
# Input:Number of elements:7
# Imput Elements: 13 5 45 7 4 56 34 
# output: 56 

def main():
 Size=int(input("Enter the size of the List"))
 print("enter the elements in the list")
 Data=list()
 for i in range(Size):
        no=int(input())
        Data.append(no)

 Max_value = Data[0]
 for i in Data:
     if i > Max_value:
         Max_value=i

 print("the Maximum value in the list is",Max_value)

if __name__=="__main__":
    main()