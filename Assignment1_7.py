def Check_divisible_by_5(number):
 return number % 5 == 0
   
def main():
    print("enter the number")
    number=int(input())
    res=Check_divisible_by_5(number)
    if res == True:
        print("ture")
    else:
        print("false")


if __name__=="__main__":
    main()   

