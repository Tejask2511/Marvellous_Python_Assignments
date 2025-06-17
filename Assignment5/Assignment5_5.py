# Even odd Checker
# write a prorgam to check wheter the enetred number is even or odd
# Expected Input: 17 
# Expected output:
# 17 is odd number

def main():
    Number=int(input("Enter the Number"))
    if Number % 2==0:
        print("the Number is Even")
    else:
        print("the Number is Odd")


if __name__=="__main__":
    main()