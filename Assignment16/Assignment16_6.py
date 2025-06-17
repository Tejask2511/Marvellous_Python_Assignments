# Write a python program to copy contents of one file(Source.txt) into another file (Destination.txt).
def main():
    
    f=open("Source.txt","w")
    f.write("Name:Tejas Prakash Kachare")
    f.close()

    f=open("Source.txt","r")
    source_contents=f.read()
    f.close()

    f2=open("Destination.txt","w")
    f2.write(source_contents)
    f2.close()



if __name__=="__main__":
    main()