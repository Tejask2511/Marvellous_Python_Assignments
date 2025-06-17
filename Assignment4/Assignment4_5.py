# write a program which contains filter() , map(), reduce() in it.
# Write a python application which contains one list of numbers
# list contains the number which are accepted from the user 
# filter shou;d filter out all the prime numbers
# map function will multiply each number by 2 
# reduce will return the maximum number from thet numbers
# (you can also use normmal function insted of lambda functions)
#Input List =[2,70,11,10,17,23,31,77]
# List after Filter=[2,11,17,23,31]
# List after map=[4,22,34,46,62]
# output of reduce = 62 


from functools import reduce

def FindMax(A,B):
    if A > B:
        return A
    else :
        return B
   

def Multiply(Number):
    return Number * 2


def ChkPrime(Num):
    if Num <= 1:
        return False
    
    for i in range(2,Num):
        if(Num % i)==0:
            return False
                         
    else:
     return True


def main():
    print("Enter the size of the list")
    Size=int(input())
    print("Enter the elements")
    Data=[]
    for i in range(1,Size+1):
        no=int(input())
        Data.append(no)

    FData=list(filter(ChkPrime,Data))
    print("filter elements are",FData)

    MData=list(map(Multiply,FData))
    print("Map elements are",MData)

    RData=reduce(FindMax,MData)
    print("reduce output is MAximum Number is ",RData)


  
if __name__=="__main__":
    main()