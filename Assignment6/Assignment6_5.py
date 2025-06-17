# accept a number from the user and check wheter it is prime or not 
# Enter a number:11
# expected output:
# 11 is a prime number

def main():
    print("Enter the Number")
    Number=int(input())

    Count=0
    for i in range(2,Number):
        if (Number % i) == 0:
            Count += 1
        
        
    if (Count == 0):
        print("Number is prime")
    else:
        print("Number is not prime")
        
        

if __name__=="__main__":
    main()