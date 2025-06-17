# write a program which accepts two file names from user. and compare contents of both the files.
# If both the files contents the same contents then display Sucess otherwise display failure.
# Accept names of both the files from commandline
# Input" Demo.txt    Hello.txt
# Compare contents of Demo.txt and Hello.txt


import sys 

def main():

    FileName=sys.argv[1]
    f1=open(FileName,"r")
    Contents_f1=f1.read()
    f1.close()

    FName=sys.argv[2]
    f2=open(FName,"r")
    Contents_f2=f2.read()  
    f2.close()

    res=Contents_f1 == Contents_f2
    if(res==True):
        print("Success")
    else:
        print("false")



if __name__=="__main__":
    main()