# Write a class rectangle with length and Width.
# Add a method to compute area and perimeter
# Area=50 , perimeter=30
 
class Rectangle:
    
    def __init__(self):
        self.Length=10
        self.Width=5

    def Calculate_Area(self):
        Area=self.Length * self.Width
        print("the Area of rectangle is:=",Area)

    def Calculate_Perimeter(self):
        Perimeter=2*(self.Length + self.Width)
        print("the Perimter of the rectangle is=",Perimeter)

    

def main():
    obj=Rectangle()
    obj.Calculate_Area()
    obj.Calculate_Perimeter()

if __name__=="__main__":
    main()