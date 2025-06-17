# Write a function that accepts a string and check whether it is palindrome 
#expected INput:
# Enter a string = radar
# expected output:
# radar is palindrome
 

def main():
    print("enter the String")
    String=str(input())
    rev=""

    for char in String:
        rev=char+rev

    if rev == String:
        print("the string is palindrome")
    else:
        print("the String is not palindrome")

if __name__=="__main__":
    main()