# write a program which accpets one number and disdplay below pattern 
# Input : 5 
# output:  *    *   *   *   *  
#          *    *   *   *   *
#          *    *   *   *   *
#          *    *   *   *   *
#          *    *   *   *   *  



def Pattern(Number):
    for i in range(Number):
        for j in range(Number):
            print("*",end="")
        print()  
  

def main():
 Number=int(input("enter the Number"))
 Pattern(Number)

 

if __name__=="__main__":
    main()
