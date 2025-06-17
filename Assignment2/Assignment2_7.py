# write a program which accepts one number asnd display below pattern 
# Input : 5 
#Output: 1     2    3    4    5
#        1     2    3    4    5
#        1     2    3    4    5
#        1     2    3    4    5
#        1     2    3    4    5

def Pattern(Number):
   for i in range(1,Number):
        for j in range(1,Number):
             print(j,end="")
        print() 


def main():
 Number=int(input(" enter the Number "))
 Pattern(Number)



if __name__=="__main__":
    main()