"""
Write a program that allows the user to navigate the lines of text in a file. The program should prompt 
the user for a filename and input the lines of text into a list. The program then enters a loop in which 
it prints the number of lines in the file and prompts the user for a line number. Actual line numbers 
range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the 
program prints the line associated with that number.
"""
def filefn(x):
    fin=open(x,"r")
    prt="y"
    lines=fin.readlines()
    while prt!="n":
        n=int(input("Enter the line number you want to print: "))
        if n==0:
            quit()
        else:
            print(lines[n])
            prt=input("Want to print any other line? y or n: ")
    
    fin.close()
def main():
    x=input("Enter the text file name: ")
    if x[-4:]!=".txt":
        x+=".txt"
    filefn(x)
if __name__=="__main__":
    main()
