# 4. Power function using recursion 
# Write a recusive function to calculate X ^ n
#  power(2,3) = 8 


# def Power_Function(a,b):
#     res=1
    
#     while b > 0 :
#          res *= a
#          b-=1
#     return res
    
res=1
def Power_function(a,b):
    global res
    if b > 0:
        res *= a
        b -= 1
        Power_function(a,b)

    return res


def main():

    res=Power_function(2,5)  
    print("the power of number is",res)   
if __name__=="__main__":
    main()