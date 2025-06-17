# Create a python program that use multiprocessing.pool to compute factorial of a number in a list 

import multiprocessing
#import multiprocessing.pool
import math

def Find_Factorial(n):
    return math.factorial(n)

def main():
    print("enter the size of the list:")
    Size=int(input())
    print(" Enter the List Elements:")
    Data=[]
    for i in range(Size):
        no=int(input())
        Data.append(no)


    with multiprocessing.Pool() as pool:
        results = pool.map(Find_Factorial,Data)


    for num,fact in zip(Data,results):
        print(f" Factorial of {num} is {fact}")

        


if __name__=="__main__":
    main()
    