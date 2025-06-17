# write a program which accepts one number from the user and check whether number is prime or not 
# Input : 5      output: Its a prime number
 

def Check_prime(Number):
    flag=0
    for i in range(2,Number):
        if Number%i==0:
            flag=1
    return flag



def main():
    Number=int(input("Enter the Number"))
    res=Check_prime(Number)
    if res == 1:
        print("the number is not prime")
    else:
        print("the number is prime")

        
if __name__=="__main__":
    main()

