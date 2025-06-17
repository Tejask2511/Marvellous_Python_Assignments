# Write a program which accepts file name from user and check whether that file exists in curretn directory or not .
# Input: Demo.txt
# check wheter demo.txt exists or not 


import os

def main():
    print("enter the file Name you want check:")
    FileName = input()

    res = os.path.exists(FileName)
    if (res == True):
        print(" file is Present:")
    else:
        print("file is not present:")

    
if __name__=="__main__":
    main()

