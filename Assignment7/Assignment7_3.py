# accept the list of numbers and use filter() to keep only even numbers.
# Expected Input: 1 2   3   4   5   6
# Expected output:
# Even Numbers=[2,4,6]


def ChkEven(Data):
    if Data % 2==0:
        return Data

def main():
    Size=int(input("Enter the size of the elements"))
    Numbers=[]
    print("Enter the Elements")
    for i in range(Size):
        no=int(input())
        Numbers.append(no)

    FData=list(filter(ChkEven,Numbers))
    print("the filter Data is:",FData)



if __name__=="__main__":
    main()