# Write a program which contains one lambda function which accepts one parameter and return power of two
# Input 4  = 16
# Input 6  = 64 

Power=lambda No:2**No

def main():
    print("enter the Number")
    Number=int(input())
    res=Power(Number)
    print("the Power of Number is",res)


if __name__=="__main__":
    main()
