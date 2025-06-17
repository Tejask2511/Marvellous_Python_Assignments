# Write a program which contains one lambda function which accepts two parameters and returns its multiplication
# INput 4 3 = 12 
# Input 6 3 = 18 


Multiplication=lambda No1,No2:No1*No2

def main():
    print("Enter The First Number")
    Number1=int(input())
    print("Enter The Second Number")
    Number2=int(input())
    res=Multiplication(Number1,Number2)
    print("the Multiplication of two Numbers is",res)


if __name__=="__main__":
    main()