# print number using Recursion
# write a recursive function to print from 1 to N 
# Expected output ( for n=5 )
# 1 2   3   4   5

 
i=1    

def Print_Num():
    global i
    if (i<=5):
        print(i)
        i+=1
        Print_Num()
    
def main():
    Print_Num()
    

if __name__=="__main__":
    main()