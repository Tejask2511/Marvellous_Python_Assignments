# Write a script to remove all blanks lines from a file. save a clean output to a new file.

def main():
    #Input_File=input(" Enter the input file:")
    #Output_File=input(" Enter the Output file:")

    f_in = open("Input_File","w")
    f_in.write("India is my country.\n")
    f_in.write("       \n")
    f_in.write("\n My name is Tejas prakash Kachare.")
    f_in.close()

    f_in=open("Input_file","r")
    f_out=open("Output_File","w")

    for line in f_in:
        if line.strip() != "":   # check if line is not empty after removing whitespace 
            f_out.write(line)


    f_in.close()
    f_out.close()


if __name__=="__main__":
    main()