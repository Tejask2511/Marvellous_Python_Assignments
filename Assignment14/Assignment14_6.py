# Create a class calculator with methods for add,substract,multiply and divide.
# Ask user input for value and call accordingly 

class Calculator:

    def __init__(self,value1,value2):
        self.Value1=value1
        self.Value2=value2


    def Addition(self):
        res=self.Value1 + self.Value2
        print("the result of the addition is:=",res)



    def Substraction(self):
        res=self.Value1 - self.Value2
        print("the result of the substraction is:=",res)


    def Multiplication(self):
        res=self.Value1 * self.Value2
        print("the result of the multiplication is:=",res)


    def Division(self):
        res=self.Value1 // self.Value2
        print("the result of the division is:=",res)
    


def main():
    
    print("choose the Operation \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division")
    choice = int(input("enter the Choice of the Operation you want to perform:"))
 
    if (choice == 1):
        print("you have chose the addition")
        value1=int(input(" Enter the first value :"))
        value2=int(input(" Enter the Second value :"))
        C1=Calculator(value1,value2) 
        C1.Addition()


    elif(choice == 2):
        print("you have choose the substraction")
        value1=int(input(" Enter the first value :"))
        value2=int(input(" Enter the Second value :"))
        C2=Calculator(value1,value2)
        C2.Substraction()

    elif( choice == 3):
        print("you have choose the multiplication")
        value1=int(input(" Enter the first value :"))
        value2=int(input(" Enter the Second value :"))
        C3=Calculator(value1,value2)
        C3.Multiplication()

    elif( choice == 4):
        print("you have choose the Division")
        value1=int(input(" Enter the first value :"))
        value2=int(input(" Enter the Second value :"))
        C4=Calculator(value1,value2)
        C4.Division()


     

if __name__=="__main__":
    main()