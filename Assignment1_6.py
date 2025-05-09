def check_num(num):
    if num>0:
        print("the number is positive")
    elif num<0:
        print("the number is negative")
    else:
        print("the number is zero")

def main():
    print("enter the number:")
    number=int(input())
    check_num(number)

if __name__=="__main__":
    main()    