# Write a program which accepts number fromm the user and returns the addtion of digits in that number
# Input: 5187934        output:37 


def Sum_of_digits(Number):
   i=Number
   sum=0
   while Number > 0:
      rem=Number%10
      sum+=rem
      Number=Number//10
   return sum   
      

def main():
 Number=int(input("enter the Number of digits"))
 res=Sum_of_digits(Number)
 print("the Addition of digits is",res)


if __name__=="__main__":
    main()