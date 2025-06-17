# Write a program which contains one class named as BookStore
# Bookstore class contains two instance variables as Name,Author
# That class contains one class variable as NOfBooks which is initialise to 0.
# There is one instance methods of class as Display whoich Displays name, Author and number of books 
# Initialise instance variable in init method by accepting the values from user as name and author .
# Inside init method increment value of NoOfBooks by one.
# After Creating the class cretae two objects of BookStore class as
# obj1=BookStore("Linux System Programming","Robert Love")
# obj1.display()      # linux system programming by Robert love. No of Books:1
# obj2.Display()      # c porgramming by dennis ritchie no of books:2  



class BookStore:

    NoOfBooks = 0

    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        BookStore.NoOfBooks +=1

    def Display(self):
        print("Name of Book:",self.Name)
        print("book Autor: ",self.Author)
        print("Number of Books:",+self.NoOfBooks)

def main():
    print("Enter the name of the book: ")
    name=input()
    print("enter the author name:")
    author=input()

    obj1 = BookStore(name,author)
    obj1.Display()

    obj2 =BookStore("Linux System Programming","robert love")
    obj2.Display()


if __name__=="__main__":
    main()
