# Accepts a number from the user and print its multiplicstion table upto 10
# Enter input
# Enter the number = 7
# Expected output
# 7 * 1 = 7
# 7 * 2 =14 
# .........
#..........
# 7 * 10 =70



def main():
    Number=int(input("Enter the Number"))
    for i in range(1,11):
        print(+Number,"*",+i,"=",Number*i)
        
if __name__=="__main__":
    main()