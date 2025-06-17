# Write a python program to create a text file named Student.txt and write the names of 5 students into it

def main():
    print("Enter the file name:")
    FileName=input()

    fobj=open(FileName,"x")
    fobj.write("Tejas\n Shubham\n Chetan\n Bhushan\n abhi")
    fobj.close()


if __name__=="__main__":
    main()