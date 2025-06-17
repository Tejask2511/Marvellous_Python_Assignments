# write a program which contains filter(),map() and reduce() in it.
# python application which contains one list of integers 
# List contains one number which are accepted from the user.Filter should filter out all such numbers which are even.
# map function will calculates its sqaure .
# reduce will return addition of that numbers
# Input List = [5,2,3,4,3,4,1,2,8,10]
#List after filter=[2,4,4,2,8,10]
# List after map=[4,16,16,4,64,100]
# output of reduce = 204


from functools import reduce

def ChkEven(Data):
     if Data%2==0:
         return Data

def Square(Data):
    return Data*Data

def Sum(A,B):
    return A+B


def main():
    print("Enter the size of the list")
    Size=int(input())
   
    print("Enter the list Elements")
    Data=[]
    for i in range(1,Size+1):
        no=int(input())
        Data.append(no)


    FData=list(filter(ChkEven,Data))
    print("Filter output is",FData)

    MData=list(map(Square,FData))
    print("Map output is",MData)

    RData=reduce(Sum,MData)
    print(" sum is",RData)


if __name__=="__main__":
    main()