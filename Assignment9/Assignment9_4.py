# Create a python program that Comapre execution time of summing Numbers from  1 to 10 million usig normal function,
# threading and multiprocessing 

import multiprocessing.process
import time
import multiprocessing
import threading


def seq():
    fans=0
    for i in range(1,10_000_001):
        fans=fans+i
        return fans
    
def M_add(l):
    fans = 0
    for num in l:
        fans=fans+num
        print("Addition is:",fans)



def main():
    print("starting Sequantial execution:")
    stime = time.time()
    ans=seq()
    print(" addition is:",ans)
    etime = time.time()
    print("Total time taken for sequential execution:",etime-stime)


    ldata=[]
    for i in range(1000000+1):
        ldata.append(i)

    print("starting Threading execution:")
    t1=threading.Thread(target=M_add,args=(ldata,))

    start_time=time.time()
    t1.start()
    t1.join()
    end_time=time.time()
    print(" total time taken by thead execution is:",end_time - start_time)

    print("Starting Multiprocessing exectution:")
    p1 = multiprocessing.Process(target=M_add,args=(ldata,))
    start_time = time.time()
    p1.start()
    p1.join()
    end_time=time.time()
    print("total time taken for multiprocessing execution is:",end_time-start_time)



if __name__=="__main__":
    main()