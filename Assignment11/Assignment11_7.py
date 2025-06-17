# *
# * *
# * * *
# * * * * 
# * * * * *



# def Print_Pattern():
#     i=1
#     while i <=5:
#         j=1
#         while j <= i:
#             print("*",end="")   
#             j=j+1
#         print("")
#         i=i+1

i=1
j=1

def Print_Pattern():
    global i, j
    if i > 5:
        return
    if j <= i:
        print("*", end="")
        j += 1
        Print_Pattern()
    else:
        print()
        i += 1
        j = 1
        Print_Pattern()
     

def main():
    Print_Pattern()

if __name__=="__main__":
     main()
