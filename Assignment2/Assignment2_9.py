# Write a program which accepts number fromm the user and returns the number of digits in that number
# Input:5187934   output: 37

def Count_Digits(Number):
 String_number=str(Number)
 Count=(len(String_number))
 
 return Count


def main():
 Number=int(input("enter the number"))
 res=Count_Digits(Number)
 print("the digits in Number is:",res)

if __name__=="__main__":
    main()
