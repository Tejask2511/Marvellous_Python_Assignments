# Write a python program using multiprocessing.process to square a list of numbers using multiple processes


import multiprocessing


def Square_Of_Numbers(number,result,index):
   result[index]= number * number


def main():
    print("enter the size of the list")
    Size=int(input())
    print("enter the list Elements:")

    Data=[]
    for i in range(Size):
        no=int(input())
        Data.append(no)


    result = multiprocessing.Array('i',len(Data))

    processes = []
    for idx,num in enumerate(Data):
        
        P1=multiprocessing.Process(target=Square_Of_Numbers,args=(num,result,idx))
        processes.append(P1)
        P1.start()

    for p in processes:
        P1.join()
        
    Squared_numbers = list(result)
    print("original numbers",Data)
    print("squared numbers",Squared_numbers)

if __name__=="__main__":
    main()