# Accpet a list of numbers and use reduce() (from functools) to find the prodcut of all numbers
# Expected Input:
# Enter list= 2  3   4
# Expected Output:
# product: 24 


from functools import reduce

def Product(X,Y):
    return X*Y

def main():
    Size=int(input("enter the size of the Number :"))
    Data=[]
    print("Enter the Elements:")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    RData=reduce(Product,Data)
    print("the product of elements is:",RData)





if __name__=="__main__":
    main()