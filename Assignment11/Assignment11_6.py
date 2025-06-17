# Sum of first N Natural Numbers 
# write a recusive function to calculate sum from 1 to N 
# sum_n(5) = 15


# def Sum_of_N(No):
#     i=1
#     sum=0
#     while i <= No:
#         sum=sum+i
#         i=i+1

#     print("the sum of N Numbers is",sum)

sum=0
i=1
def Sum_of_N(No):
    global sum
    global i
    if i <= No:
        sum=sum+i
        i=i+1
        Sum_of_N(No)
    return sum



def main():
    res=Sum_of_N(5)
    print("the sum of n numbers is",sum)



if __name__=="__main__":
    main()