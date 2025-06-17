# write a program which accepts file name from user and open that file and display the contents of that file on screen 
# Input: Demo.txt 
# output: Display the contents of the file on console


def main():
    print("enter the file name:")
    FileName=input()

    fobj=open("Demo.txt.txt" , "r")
    content=fobj.read()
    print(content)
    


if __name__=="__main__":
    main()