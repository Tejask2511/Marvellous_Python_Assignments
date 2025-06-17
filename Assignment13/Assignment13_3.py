#3. Write a program which contains one class named as Numbers.
#Arithmetic class contains one instance variables as Value.
#Inside init method initialise that instance variables to the value which is accepted from user.
#There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors), Factors)•
#ChkPrime() method will returns true if number is prime otherwise return false.
#ChkPerfect) method will returns true if number is perfect otherwise return false.
#Factors) method will display all factors of instance variable.
#SumFactors method will return addition of all factors. Use this method in any another method as a helper method if required.
#After designing the above class call all instance methods by creating multiple objects.

class Numbers:

    def __init__(self,no):
        self.Value=no


    def ChkPrime(self):
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return True
            else:
                return False


    def ChkPerfect(self):     
        sum=0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                sum=sum+i
                
        if sum == self.Value:
            return True
        else:
            return False
                


    def Factors(self):
        
        for i in range(1,self.Value):
            if self.Value % i == 0:
                print(i)
        
        
    def SumFactors(self):
        sum=0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                sum= sum + i 
        print("the sum of the factors is:",sum)



def main():
    print("enter the Number:")
    no=int(input())

    No1 = Numbers(no)    # object creation

    res=No1.ChkPrime()
    if(res==True):
        print("the Number is not prime")
    else :
        print("the number is prime:")


    res=No1.ChkPerfect()
    if(res==True):
        print("The Number is perfect Number")
    else:
        print("the number is not perfect")


    No1.Factors()
    No1.SumFactors()


if __name__=="__main__":
    main()
