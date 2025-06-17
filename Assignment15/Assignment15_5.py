# Accept file name and one string from user and return the frequency of the string from file.
# Input Demo.txt Marvellous
# Search Marvellous in Demo.txt
 
import sys

def main():
    FileName=sys.argv[1]
    Search_String=sys.argv[2]

    f=open(FileName,"r")
    Contents=f.read()
    f.close()
    
    Words=Contents.split()                     # Splits contents into words

    Frequency=Words.count(Search_String)       #Count the Frequency of the Search String

    print(f" the World occured { Frequency} times in the file ")



if __name__=="__main__":
    main()