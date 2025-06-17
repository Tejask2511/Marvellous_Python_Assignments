#Create a class variable with method start().Derive class Car and override the method start() 
# with additional behaviour.show method overriding

class Vehicle:

    def Start(self):
        print("Start method in vehicle class")


class Car:

    def Start(self):
        print("start method in car class")



def main():
    
    v=Vehicle()

    c=Car()

    v.Start()
    c.Start()


if __name__=="__main__":
    main()