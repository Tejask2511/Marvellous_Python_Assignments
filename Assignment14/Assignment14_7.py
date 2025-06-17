#Create a base class person with name And age.Derive a class teacher with subject and salary.
# use super() to call base class constructor and print both 

class Person:

    def __init__(self,name,age):
        print("control in person init method")
        self.Name=name
        self.Age=age

    def Display(self):
        print("In person Display method")
        print("Name is:",self.Name)
        print("Age is:",self.Age)


class Teacher(Person):

    def __init__(self,name,age,sub,salary):
        print("control in teacher init method")
        self.Subject=sub
        self.Salary=salary
        super().__init__(name,age)

    def Display(self):
        print("In Teacher Display method")
        super().Display()
        print("Subject is:",self.Subject)
        print("Salary is:",self.Salary)
       


def main():

    T1=Teacher("Tejas","24","English",25000)
    T1.Display()

    


if __name__=="__main__":
    main()