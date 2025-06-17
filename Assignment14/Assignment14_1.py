# Create a class employee with attirubutes name,emp_id,and salary.
# creates object of this class and print their details using method
#Expected output :
#Name:Rohit,ID:101,Salary:500000 

class Employee:

    def __init__(self,name,id,salary):
        self.Name=name
        self.ID=id
        self.Salary=salary

    def Display(self):
        print("Name:",self.Name)
        print("ID:",+self.ID)
        print("Salary:",+self.Salary)


def main():
    print("enter the employee name")
    name=input()
    print("Enter the employee id:")
    id=int(input())
    print("enter the salary")
    salary=int(input())

    Emp=Employee(name,id,salary)
    Emp.Display()


if __name__=="__main__":
    main()