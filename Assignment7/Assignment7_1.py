# Write two lambda functions:
# one to calculate square of number
# Another to calculate cube of a number
# Expected Input 
# Enetr a number
#Expected output 
#Square :9
# cube:27



Cal_Square=lambda Number:Number*Number

Cal_Cube=lambda Number:Number*Number*Number

def main():
    print("enter the Number")
    Number=int(input())
    res=Cal_Square(Number)
    print("the Square of the Number is:",res)


    Ans=Cal_Cube(Number)
    print("the Cube of NUmber is",Ans)



if __name__=="__main__":
    main()