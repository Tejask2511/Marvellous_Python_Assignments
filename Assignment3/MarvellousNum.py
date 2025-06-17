def ChkPrime(Num):
    if Num < 1:
        return False
    
    for i in range(2,Num):
        if(Num % i)==0:
            return False
                         
    else:
     return True

