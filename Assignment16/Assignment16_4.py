# Accept 10 numbers from user and write them into a file named numbers.txt,each on a new line 
def main():
    print("Enter the 10 Numbers:")

    f=open("Numbers.txt","w")

    for i in range(1,11,1):
        num=input()
        f.write(num +"\n")
    f.close()


        
if __name__=="__main__":
    main()