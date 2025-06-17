# write a program which accepts one number from the user and return its factortial
# Input : 5      OUtput: 120

def Find_factorial(Number):
    fact=1
    i=1
    while i <= Number:
     fact=fact*i
     i+=1

    return fact


def main():
 Number=int(input("enter the Number"))
 res=Find_factorial(Number)
 print("the factorial of a number is",res)

if __name__=="__main__":
    main()
