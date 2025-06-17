# design python application which creates two threads as Even,odd List.
# both the threads acceptt list of integer as a parameter.Evenlist  thread and and all even elements from input list 
# and display the addition odd list thread add all odd elements from input list and display the addition


import threading

def Even_List(Data):
    sum=0
    for num in Data:
        if num % 2 == 0:
            sum = sum+num
    print("the addition of even elements from list is",sum)


def Odd_List(Data):
    sum=0
    for num in Data:
        if num % 2 != 0:
            sum=sum+num
    print("the addition of odd elements from list is",sum)



def main():
    print("Enter the size of the list")
    Size=int(input())
    print("enter the elements of the list")
    Data=[]
    for i in range(Size):
        no=int(input())
        Data.append(no)

    T1=threading.Thread(target=Even_List,args=(Data,))
    T2=threading.Thread(target=Odd_List,args=(Data,))

    T1.start()
    T1.join()

   
    T2.start()
    T2.join()


if __name__=="__main__":
    main()