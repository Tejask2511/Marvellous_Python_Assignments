# Design python application which creates a two thread named as even and odd.
#  Even thread will display first 10 even numbers,and odd thread will display first 10 odd numbers

import threading

def Print_Even():
    print("the first 10 even numbers are:")
    count=0
    i=1
    while i >= count:
        if i % 2 == 0:
            print(i)
            count += 1
            if count == 10:
             break
        i+=1

def Print_Odd():
    print("the first ten Odd Numbers are:")
    count=0
    i=1
    while i>= count:
        if i % 2 != 0:
            print(i)
            count += 1
            if count == 10:
                break
        i+=1



def main():
    T1=threading.Thread(target=Print_Even,args=())
    T2=threading.Thread(target=Print_Odd,args=())
    T1.start()
    T1.join()

    T2.start()
    T2.join()



if __name__=="__main__":
    main()