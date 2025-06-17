# create module named as arithmatic which contains 4 functions.
#  Add() for addition sub() for substractionn mul() for multiplication div()for division.
# all functions accepts two parameter as number and perfrom the operation.
# write one python program which call all functions from arithmatic modules by accepting the parameters from the user

import Arithmatic

def main():
 Number1=int(input("enter the first number"))
 Number2=int(input("enter the second number"))

 res=Arithmatic.Add(Number1,Number2)
 print("the addition is",res)

 res=Arithmatic.Sub(Number1,Number2)
 print("the Substraction is",res)

 res=Arithmatic.Mul(Number1,Number2)
 print("the Multiplication is",res)
 
 res=Arithmatic.Div(Number1,Number2)
 print("the division is",res)


if __name__=="__main__":
    main()