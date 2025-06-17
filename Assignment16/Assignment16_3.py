# Write python script to count number of lines,words,and characters in given file 

def main():
    File_Name=input("Enter the File Name:")

    f=open(File_Name,"r")

    line_count = 0
    words_count = 0
    char_count =0

    for line in f:
        line_count += 1                  # counts the Line
        char_count += len(line)          # counts character including spaces and newline

        in_word =False
        for char in line:
            if char.isspace():
                in_word=False
            elif not in_word:
                words_count += 1
                in_word = True


    f.close()
    print("Number of Lines:",line_count)
    print("Number of Words:",words_count)
    print("Number of characters:",char_count)



if __name__=="__main__":
    main()