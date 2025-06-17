# count zeros in a number ( Recursivly)
# Write a recusive function to calculate how many Zeros given in the number
# count_zeros(1020300) = 4 




# def main():
#     count = 0
#     No=2020205600
#     i=1
#     while No > 0:
#         rem=No%10
#         if rem == 0:
#             count += 1
#         No=No//10

#     print(+count," zeros in number")

Count=0
def Zeros_Count(Number):
    global Count
    if(Number > 0):
        rem=Number % 10
        if rem == 0:
            Count += 1
        Number = Number // 10
        Zeros_Count(Number)

    return Count

    
def main():
    res=Zeros_Count(2020205600)
    print("the Number of Zeros Present in the Number is:",res)




if __name__=="__main__":
    main()