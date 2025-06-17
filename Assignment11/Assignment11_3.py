# Sum of Digits 
# write a recursive function to calculate the sum of digits of a number

sum=0
def Digit_Sum(No):
    i= No
    global sum
    if No > 0:
        rem=No % 10
        sum=rem+sum
        No = No // 10
        Digit_Sum(No)

    return sum
    


def main():
    res=Digit_Sum(3222)
    print("the sum of the Digits is:",res)

    
    
if __name__=="__main__":
    main()