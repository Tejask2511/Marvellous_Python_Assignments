#create a class book with private attirubute _price. 
# add methdos to get and set the price.show encapsulation 

class Book:

    def __init__(self):
        self._Price=0

    def Set_Price(self,price):
        self._Price=price

    def Get_Price(self):
        return self._Price
    
    

def main():

    boj=Book()

    print("Enter the price of the book:")
    price=int(input())

    boj.Set_Price(price)
    res=boj.Get_Price()
    print("the set value of book is:",res)

    

if __name__=="__main__":
    main()