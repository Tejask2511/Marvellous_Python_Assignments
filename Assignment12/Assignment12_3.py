#Write a program which contains one class named as Arithmetic.
#Arithmetic class contains three instance variables as Valuel ,Value2.
#Inside init method initialise all instance variables to 0.
#There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division.
#Accept method will accept value of Valuel and Value2 from user.
#Addition() method will perform addition of Value, Value2 and return result.
#Subtraction) method will perform subtraction of Valuel, Value2 and return result.
#Multiplication) method will perform multiplication of Valuel, Value2 and return result.
#Division) method will perform division of Value, Value2 and return result.
#After designing the above class call all instance methods by creating multiple objects.


class Arithmatic:

    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        self.value1=int(input("enter the value 1:"))
        self.value2=int(input("enter the value 2:"))
        


    def Addition(self):
        res= self.value1 + self.value2
        return res



    def Substraction(self):
        res= self.value1 - self.value2
        return res
        

    
    def Multiplication(self):
       res=self.value1 * self.value2
       return res


    def Division(self):
        res=self.value1 // self.value2
        return res

    



def main():
    A1=Arithmatic()   #object creation
    A1.Accept()
    res=A1.Addition()
    print("the addtition of two number is:",res)

    res=A1.Substraction()
    print("the substraction of two number is:",res)

    res=A1.Multiplication()
    print("the multiplication of two number is:",res)

    res=A1.Division()
    print("the Division of two number is:",res)



if __name__=="__main__":
    main()