# Design python application which creats three threads as small,capital,digits.
# all the thread accept string as a parameter.small thread dispaly number of small characters,
# capital thread display number of capital character and digit threads display number of digits,
# display id and name of each thread

import threading

def Small(S):
    print(" Thread ID of Small thread is:",threading.get_ident())
    count=0
    for ch in S:
        if ch.islower():
            count += 1
    print("the count of the Small lettes in string is:",count)


def Capital(S):
    print(" Thread ID of Capital thread is:",threading.get_ident())
    count=0
    for ch in S:
        if ch.isupper():
            count += 1
    print("the count of upper letters in string is:",count)


def Digit(S):
    print(" Thread ID of Digit thread is:",threading.get_ident())
    count=0
    for ch in S:
        if ch.isdigit():
            count += 1
    print("the count of digits in the string is:",count)
    

def main():
    print(" Enter the string:")
    String=str(input())

    T1=threading.Thread(target=Small,args=(String,))
    T2=threading.Thread(target=Capital,args=(String,))
    T3=threading.Thread(target=Digit,args=(String,))

    T1.start()
    T2.start()
    T3.start()
    
    T1.join()
    T2.join()
    T3.join()


if __name__=="__main__":
    main()
