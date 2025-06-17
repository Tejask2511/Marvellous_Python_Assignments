# Write a prpgram which contains filter(), map() and reduce() in it.
# python application which contains on list of numbers.
# list contains the number which are accepted from user.
# Filter should filter out all such numbers which is greter than or aequal to 70 
# and less than or equal to 90.map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List =[4,34,36,76,68,24,89,23,86,90,45,70] 
# List after filter=[76,89,86,90,70]
# List after Map=[86,99,96,100,80]
# output of reduce=6538752000

from functools import reduce

def Increase(Data):
    return Data + 10
    
def Chkrange(Data):
    return 75 <= Data <= 90 

def Product(x,y):
    return x*y


def main():
    print("Enter the size of the Elements")
    Size=int(input())
    print("Enter the list Elements")
    Data=[]
    for i in range(1,Size+1):
        no=int(input())
        Data.append(no)

    FData=list(filter(Chkrange,Data))
    print("filter output",FData)

    MData=list(map(Increase,FData))
    print("Map output is",MData)

    RData=reduce(Product,MData)
    print("prodcut of all Elements is",RData)

       
    
if __name__=="__main__":
    main()
