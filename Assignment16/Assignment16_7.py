# Cretate a file Marks.txt with student name and marks.Then read the file and display students who scored more than 75 marks.
def main():

    f=open("Marks.txt","w")

    for i in range(5):
        Name=input("Enter the name of Student:")
        Marks =input("Enter the Marks")
        f.write(f"{Name} {Marks}\n")

    f.close()


    f=open("Marks.txt","r")
    for line in f:
        Name,Marks =line.split()
        if int(Marks) > 75:
            print(Name,"=",Marks)

    f.close()



if __name__=="__main__":
    main()