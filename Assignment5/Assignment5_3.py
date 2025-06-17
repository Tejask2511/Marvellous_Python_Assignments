# voting Elligibility checker
# Accept age from the user and check wheter the person elligible to vote:( Age Should be 18 or above>)
# Expected input:
# Enter age:19
# Expected Output:
# elligible to vote 

def main():
    age =int(input("Enter the Age"))

    if age >= 18:
        print("the person is elligible to vote")
    else:
        print("person is not elligible to vote")


if __name__=="__main__":
    main()
