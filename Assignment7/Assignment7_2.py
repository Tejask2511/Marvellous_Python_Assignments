# accept a list of integers from the user and map() function to double each value 
# Expected Input
# Enter list : 1    2   3   4   5
# expected output
#Double list : 2    4   6   8   10

def Double_value(Number):
    return Number+Number


def main():
    Size=int(input("Enter The Size Of List"))
    Number=[]
    print("Enter The Elements")
    for i in range(Size):
        no=int(input())
        Number.append(no)

    MData=list(map(Double_value,Number))
    print("the Double data is:",MData)


if __name__=="__main__":
    main()