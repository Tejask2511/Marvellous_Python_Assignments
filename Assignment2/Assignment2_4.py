# Write a program which accpets one number from the user and returns the addition of its factors 
# Input: 12      output: 16  ( 1+2+3+4+6) 

def Factor_addition(Number):
    sum=0
    i=1
    while i < Number:
        if Number%i==0:
            sum+=i
        i=i+1
    return sum
        

def main():
    Number=int(input("Enter the Number"))
    res= Factor_addition(Number)
    print("the factors addition is",res)


if __name__=="__main__":
    main()
