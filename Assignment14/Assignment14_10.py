#Demonstrate Private,protected public access modifiers using a class employee 
# with attributes:__Salary ,_deparment ,name 

class Employee:

    def __init__(self,name ,department,salary):
        self.Name=name                               # public 
        self._department=department                  #protected
        self.__Salary=salary                         #private


    def Get_Salary(self):
        return self.__Salary
    


def main():

    Emp1=Employee("Tejas","IT",80000)

    print("public Access:=",Emp1.Name)

    print(" protected Access:=",Emp1._department) 

  #  print(" private Access :=",Emp1.__Salary)     not allowed to access 

    Salary= Emp1.Get_Salary()
    print("the Salary is:",Salary)






if __name__=="__main__":
    main()