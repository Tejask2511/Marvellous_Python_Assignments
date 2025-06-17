# vowels or consonant check 
# Accepts a single character from the user and check if it is vowels ( a,e,i,o,u).if not then print it is constant.
# Expected output
# Enter a character:e
# Expected output:
# 'e ' is vowel
#  



def main():
    print("enter the character:")   
    ch = str(input())

    if ch in 'aeiouAEIOU' :
        print(" char is vowel")
    else:
        print(" it is consonant")



if __name__=="__main__":
    main()