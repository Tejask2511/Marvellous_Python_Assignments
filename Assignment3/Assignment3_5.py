# Write a program which accepts n number from user and store it into list.
# return addition of all prime numbers from the list
# main pyhton file accepts n numbers from the user and pass each number to check prime function
#  which is a part of out user defiend module named as MarvellousNum. Name of the function from main python file should be listprime().
# Input Number of elements:11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8 
# output: 54(13+5+7+2+5)   


from MarvellousNum import ChkPrime

def main():
 size=int(input("enter the size of the list"))
 
 #Data=list()
 Data=[]
 for i in range(size):
    no=int(input("enter the numbers"))
    Data.append(no)

 sum=0
 for i in Data:
     if ChkPrime(i):
      sum+=i

 print("sum of all prime numbers from the list is",sum)
 
 
if __name__ == "__main__":
    main()