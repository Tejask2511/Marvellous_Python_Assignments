# Write a program to display the content of file Data.txt

def main():
    print("enter the file name:")
    FileName=input()

    f=open(FileName,"w")
    f.write("India is my country:")
    f.close()

    f=open(FileName,"r")
    Content=f.read()
    print(Content)
    f.close()
    


if __name__=="__main__":
    main()