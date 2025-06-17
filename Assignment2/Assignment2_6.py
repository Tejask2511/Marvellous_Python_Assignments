# write a program which accpets one number and display below pattern 
# Input: 5 
#   *   *   *   *   *
#   *   *   *   *
#   *   *   *
#   *   *
#   *

def Pattern(Number):
    for i in range(Number):
        for j in range(i,Number):
            print("*",end="")
        print()


def main():
    Number=int(input("Enter the Number"))
    Pattern(Number)


if __name__=="__main__":
    main()

