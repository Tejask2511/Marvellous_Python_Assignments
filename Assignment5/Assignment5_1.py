# Arithmatic operations on two number
# Write  a program to accept two integers from the user and display their:
# sum 
# Difference
# product
# Division

# Expected INput:
# Enter first Number:10
# enter second Number:2 
 # Expected Output:
# Sum: 12
# Difference:8 
# product: 20 
# Division: 5.0 


def main():
     Number1=int(input("Enter the first Number"))
     Number2=int(input("Enter the second Number"))

     Addition = Number1 + Number2
     print("the addition of two numbers is:",Addition)

     Difference = Number1 - Number2
     print("the Difference of numbers is :",Difference)

     Product = Number1 * Number2
     print("the product of two numbers is:",Product)

     Division = Number1 // Number2
     print("the Division of Number is:",Division)

    

if __name__=="__main__":
    main()