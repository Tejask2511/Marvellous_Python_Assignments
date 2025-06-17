# Design python application which contains two threads named as thread1 and thread 2
#thread1 dispaly 1 to 50 on screen and thread 2 display 50 to 1 in reverse order on screen.
# After execution of thread1 gets completed the schedule thread2

import threading

def Display():
    print("Numbers from 1 to 50")
    i=1
    while i <= 50:
        print(i)
        i+=1

def Display2():
    print("reverse number from 50 to 1")
    i=50
    while i >= 1:
        print(i)
        i-=1


def main():

    T1=threading.Thread(target=Display,args=())
    T2=threading.Thread(target=Display2,args=())

    T1.start()
    T1.join()


    T2.start()
    T2.join()



if __name__=="__main__":
    main()