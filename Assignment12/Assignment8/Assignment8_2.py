# Design python application which creates two threads as evenfactor and oddfactor.
#both the thread accepts 1 parameter as integer.EvenFactor thread will display addition of even factors of given number 
# and odd factor will display addition of odd factors of a given number.After execution of both the thread gets Completed main thread 
# should display message of exit from main  

import threading
def Even_Factor(Num):
    sum=0
    for i in range(1,Num+1):
        if Num % i==0:
            if i % 2==0:
                sum=sum+i
    
    print("the addition of even factors of given number is:",sum)


def Odd_Factor(Num):
    sum=0
    for i in range(1,Num+1):
        if Num % i == 0:
            if i % 2 !=0:
                sum=sum+i

    print("the addition of Odd factors of given number is:",sum)


def main():
    T1=threading.Thread(target=Even_Factor,args=(10,))
    T2=threading.Thread(target=Odd_Factor,args=(10,))

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    print("Exit From main")

    
if __name__=="__main__":
    main()