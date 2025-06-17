# Create a python program that starts three threads,
# each printing numbers from 1 to 5 with delay of 1 second . use threading.Thread


import threading
import time

def Print_Numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)


def main():

    T1=threading.Thread(target=Print_Numbers,args=())
    T2=threading.Thread(target=Print_Numbers,args=())
    T3=threading.Thread(target=Print_Numbers,args=())

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("All threads have finished execution")


if __name__=="__main__":
    main()