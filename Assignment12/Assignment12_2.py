# Write a program which contains one class named as Circle.
#Circle class contains three instance variables as Radius, Area, Circumference.
#That class contains one class variable as PI which is initialise to 3.14.
#Inside init method initialise all instance variables to 0.0.
#There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display().
#Accept method will accept value of Radius from user.
#CalculateAre() method will calculate area of circle and store it into instance variable Area.
#CalculateCircumference) method will calculate circumference of circle and store it into instance variable Circumference.
#And Display) method will display value of all the instance variables as Radius, Area, Circumference.
#After designing the above class call all instance methods by creating multiple objects.



class Circle:
    PI=3.14

    def __init__(self):
        self.radius=0
        self.area=0
        self.Circumference=0


    def Accept(self):
        print("enter the radius:")
        self.radius=int(input())


    def CalculateArea(self):
        self.area=Circle.PI*self.radius*self.radius

    
    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.radius


    def Display(self):
        print("the value of radius is:",+self.radius)
        print("the value of area is:",+self.area)
        print("the value of Circumference is:",+self.Circumference)



def main():
    
    c1=Circle()  #object creation
    c1.Accept()
    c1.CalculateArea()
    c1.CalculateCircumference()
    c1.Display()

    c2=Circle()   #object creation
    c2.Accept()
    c2.CalculateArea()
    c2.CalculateCircumference()
    c2.Display()



if __name__=="__main__":
    main()