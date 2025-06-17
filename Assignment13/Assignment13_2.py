#2. Write a program which contains one class named as BankAccount.
#BankAccount class contains two instance variables as Name & Amount.
#That class contains one class variable as ROI which is initialise to 10.5.
#Inside init method initialise all name and amount variables by accepting the values from user.
#There are Four instance methods inside class as Display(), Deposit(), Withdraw(),CalculateIntrest).
#Deposit() method will accept the amount from user and add that value in class instance variable Amount.
#Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
#• CalculateIntrest) method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
#And Display() method will display value of all the instance variables as Name and Amount.
#After designing the above class call all instance methods by creating multiple objects.

class Bank_Account:
    ROI=10.5

    def __init__(self,name,amount):
        self.Name=name
        self.Amount=amount

    
    def Deposite(self,Deposite_amount):
        self.Amount += Deposite_amount

    
    def Withdraw(self,withdrwan_amount):
        self.Amount -= withdrwan_amount
        return self.Amount


    def CalculateIntrest(self,time):
        intrest=(self.Amount * Bank_Account.ROI * time)/100
        return intrest


    def Display(self):
        print("Name of Acc Holder:",self.Name)
        print("ammount is:",+self.Amount)


def main():
    print("Enter the Acc holder name:")
    name=input()
    print("Enter the amount:")
    amount=int(input())

    acc1=Bank_Account(name,amount)

    Deposite_amount=int(input("enter the deposite amount:"))
    acc1.Deposite(Deposite_amount)

    withdrawn_amount=int(input("Enter the withdrawn amount:"))
    res=acc1.Withdraw(withdrawn_amount)
    print("the amount after withdrwan is",res)

    print("enter the time(in years) to calculate intrest:")
    time=float(input())

    res_Intrest=acc1.CalculateIntrest(time)
    print(f"intrest for {time} years is {res_Intrest}")

    acc1.Display()


if __name__=="__main__":
    main()