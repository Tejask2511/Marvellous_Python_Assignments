# Write a program which accepts one number and display below pattern 
# Input: 5
# output: 1    
#         1    2
#         1    2    3
#         1    2    3    4
#         1    2    3    4    5 

def Pattern(Number):
    for i in range(1,Number+1):
         for j in range(1,i+1):
              print(j,end="")
         print()



def main():
 Number=int(input("Enter the Number"))

 Pattern(Number)


if __name__=="__main__":
    main()