# write a functions that accepts a list of integers adn returns a list of prime numbers using filter()
# expected Input:
# Enter list: 10    11  12  13  14  15  16  17  
# Expected output:
#prime NUmbers:[11,13,17]

def Find_Prime(Data):
    Count=0
    for i in range(2,Data):
        if (Data % i) ==0:
            Count+=1 
      
    if(Count == 0):
        return True
    else:
        return False   


def main():
    Size=int(input("Enter the Size of the elements:"))
    Data =[]
    for i in range(Size):
        no=int(input())
        Data.append(no)

    FData=list(filter(Find_Prime,Data))
    print("the list of Prime Number is:",FData)



if __name__=="__main__":
    main()