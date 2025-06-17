# Write a program which accepts file name from user and create new file named as Demo.
# txt and copy all contents from exisiting file into the new file.Accept file name through command line arguments>
# Input: Abc.txt 
# Create new file as demo.txt and copy contents of Abc.txt in Demo.txt

import sys

def main():

    FileName= (sys.argv[1])

    f=open(FileName,"x")
    f.write("this contents writen in abc,txt= my name is tejas prakash kachare")
    f.close()


    f=open(FileName,"r")
    contents_Abc=f.read()
    f.close()



    fobj=open("Demo.txt","w")
    fobj.write(contents_Abc)
    fobj.close()





if __name__=="__main__":
    main()