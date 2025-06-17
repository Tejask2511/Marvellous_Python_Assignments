# Accept 5 numbers from the user.find and print the largest number
# expetced Input:
# enter 5 numbers : 23 89 12 56 45 
# expected output:
# Maximum number is:89 

def main():
    Size=int(input(("Enter the size of the Numbers")))
    Numbers=[]
    print("enter elements:")
    for i in range(Size):
        no=int(input())
        Numbers.append(no)

    Max=Numbers[0]
    for Num in Numbers:
        if Num > Max:
            Max=Num
    
    print("the Largest Number is:",Max)


if __name__=="__main__":
    main()