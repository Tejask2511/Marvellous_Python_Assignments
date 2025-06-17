# Area and perimeter of the rectangle
# Accept the length and width of the rectangle. calculate and display the area and perimeter 
# expected Output:
# enter Length:5
# enter widht:3
# Expected Output:
# Area=15
# perimter=16



def Area(Length,Width):
    res=Length*Width
    return res

def Perimeter(Length,Width):
    res=2*(Length+Width)
    return res

def main():
    Length=int(input("Enter the Length"))
    width=int(input("Enter the Width"))
    res=Area(Length,width)
    print("the area is",res)

    ans=Perimeter(Length,width)
    print("the perimeter is",ans)

if __name__=="__main__":
    main()