# Find Largest amoung three numbers:
# accept three numbers from user and print largest number using nested if else statements.
# Expected Input:
# Enter three numbers: 5 9 3
# Expected output: 
# Largest Number is 9.


def main():
    Number1=int(input("Enter the first Number"))
    Number2=int(input("Enter the second Number"))
    Number3=int(input("Enter the third Number"))

    if Number1 > Number2 and Number1 > Number3:
        print(+Number1," is greter")
    
    elif Number2 > Number1 and Number2 > Number3:
        print(+Number2," is greter")

    elif Number3 > Number1 and Number3 > Number2:
        print(+Number3," is greter")



if __name__=="__main__":
    main()