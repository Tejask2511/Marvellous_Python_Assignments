def Add(number1,number2):
    res=number1+number2
    return res

def main():
    print("enter the first number")
    number1=int(input())

    print("enter the second number")
    number2=int(input())

    res=Add(number1,number2)
    print("the addition of two numbers is",res)

if __name__=="__main__":
    main()
        
