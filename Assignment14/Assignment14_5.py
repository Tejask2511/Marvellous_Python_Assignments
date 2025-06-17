#Create a class Bank Account with account Number,name and balance. 
# use __init__ and create methods for deposite,withdraw and displaying balance

class Bank_Account:

    def __init__(self,acc_no,name,bal):

        self.Acc_No = acc_no
        self.Acc_Holder_Name = name
        self.Bal = bal

    def Deposite(self,amount):
        self.Bal += amount

    def Withdraw(self,amount):
        self.Bal -= amount

    
    def Display_Info(self):
        print("Account No :=",self.Acc_No)
        print("Account Holders name :=",self.Acc_Holder_Name)
        print("Account Bal:=",self.Bal)

    

def main():
    
    acc1=Bank_Account(1,"Tejas",5000)
    acc1.Display_Info()

    print("enter the amount you want to deposite:")
    Deposite_amount=int(input())
    acc1.Deposite(Deposite_amount)

    acc1.Display_Info()

    print("Enter the amount you want to withdraw:=")
    amount=int(input())
    acc1.Withdraw(amount)
    
    acc1.Display_Info()






if __name__=="__main__":
    main()