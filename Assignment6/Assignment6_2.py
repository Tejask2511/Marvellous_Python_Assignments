# Print Sum of even numbers between 1 to 100.use a loop to find and print the sum of all even numbers from 1 to 100 
# Expected Output:
# sum of even numbers between 1 to 100 is: 2550


def main():
    sum=0
    i=1
    while i <=100:
        if i % 2 == 0:
            sum=sum+i
        i+=1

    print("the sum of all even Numbers between 1 To 100 is:",sum)

if __name__=="__main__":
    main()