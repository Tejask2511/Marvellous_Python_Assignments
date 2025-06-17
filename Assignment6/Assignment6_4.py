# accept a number and prints its factorial using a for loop 
# expected Input:
# Enter a number 5
# Expected output:
# factorial of 5 is : 120
 

def main():
    Number=int(input("Enter the Number"))
    fact=1
    for i in range(1,Number+1):
        fact=fact*i
    print("factorial of Number is:",fact ) 


if __name__=="__main__":
    main()