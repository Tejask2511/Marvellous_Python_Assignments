# Write a program to read a file line by line and display only those lines that contains more than 5 words

def main():

    f =open("Data.txt","r")

    for line in f:
        Words=line.split()
        if len(Words) >= 5:
            print(line,end="")

    f.close()





if __name__=="__main__":
    main()