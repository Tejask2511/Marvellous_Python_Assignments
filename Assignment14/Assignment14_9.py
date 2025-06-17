#Create a class product with attributes name and price.implement __Eq __ method to comapre two Product
#  if they are equal in price 

class Product:

    def __init__(self,Name,price):
        self.Name=Name
        self.Price=price


    def __eq__(self, value):
        if self.Name == value.Name and self.Price == value.Price:
            return True
        else:
            return False

    

def main():
    p1=Product("fan",5000)

    p2=Product("fan",5000)

    print(p1 == p2)

    

if __name__=="__main__":
    main()