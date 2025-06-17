#1. Write a program which contains one class named as Demo.
#Demo class contains two instance variables as nol, no2.
#That class contains one class variable as Value.
#There are two instance methods of class as Fun and Gun which displays values of instance variables.
#Initialise instance variable in init method by accepting the values from user.
#After creating the class create the two objects of Demo class as
#Obj1 = Demo(11,21)
#Obj2 = Demo(51,101)
#Now call the instance methods as
#Obj1. Fun()
#Obj2. Fun()
#Obj1.Gun()
#Obj2. Gun()



class Demo:
    value=0     # class variable

    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2


    def fun(self):
        print(" we are in fun method:")
        print("value 1 is",+self.no1)
        print("value 2 is",self.no2)


    def gun(self):
        print(" we are in gun method:")
        print("value 1 is",+self.no1)
        print("value 2 is",self.no2)

        

def main():
    no1=int(input("Enter the no1 value"))
    no2=int(input("enter the no2 value"))
    
    obj1 = Demo(no1,no2)    # object creation
    obj2 = Demo(51,101)    # object creation

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()


if __name__=="__main__":
    main()