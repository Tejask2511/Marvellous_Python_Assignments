# Factorial using recursion 
# Write a recursive function to calculate factorial of a number
# factorial(5) = 120

fact =1
def Find_Fact(No):
    global fact
    i=No
    if i >= 1 :
        fact=fact*i
        No-=1
        Find_Fact(No)
    return fact


def main():
    res=Find_Fact(5)
    print("the factorial of Number is",res)

if __name__=="__main__":
    main()