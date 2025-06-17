#Create a class student with name,roll_No and class Variable School_name.
# print students details and school name.change the school name using class name 

class Student:
    School_Name="K.N.V"


    def __init__(self,name,roll_no):
        self.Name=name
        self.Roll_No=roll_no

    def Dipslay_Info(self):
        print("Student name is:",self.Name)
        print("studdnt roll no:",self.Roll_No)
        print("School name:",Student.School_Name)

    def Set_School_Name(self,s_name):
        Student.School_Name=s_name

   
    def Get_School_Name(self):
        return Student.School_Name
    


def main():
    
    print("we are in main:")

    S1=Student("Tejas",25)
    S1.Dipslay_Info()

    S1.Set_School_Name("DYP")
    s_name =S1.Get_School_Name()
    print("After changing the school name is:",s_name)



if __name__=="__main__":
    main()