def ChkNum(num):
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")

def main():
    print("enter the number")
    number=int(input())
    ChkNum(number)

if __name__=="__main__":
    main()            
    