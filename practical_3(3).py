"""
Write a script named dif.py. This script should prompt the user for the names of two text files 
and compare the contents of the two files to see if they are the same. If they are, the script 
should simply output "Yes". If they are not, the script should output "No", followed by the first 
lines of each file that differ from each other. The input loop should read and compare lines from each 
file. The loop should break as soon as a pair of different lines is found. 
"""
import os.path
from os import path 
import filecmp
x,y=input("Enter names of two text files without .txt extension: ").split()
#A file exits or not
if x[-4:]!=".txt":
    x+=".txt"
if y[-4:]!=".txt":
    y+=".txt"
while True:
    if(path.exists(x)) and (path.exists(y)):
        f=open(x,"r")
        g=open(y,"r")
        comp=filecmp.cmp(x,y,shallow=False)
        if comp:
            print("YES")
        else:
                f_line1=f.readline()
                g_line1=g.readline()
                # Loop if either file1 or file2 has not reached EOF
                while f_line1 != '' or g_line1 != '':
                    # Strip the leading whitespaces
                    f_line1 = f_line1.rstrip()
                    g_line1 = g_line1.rstrip()
                    # Compare the lines from both file
                    if f_line1 != g_line1:
                        print("NO")
                        print("The different line from first file is: \n\n",f_line1)
                        print("The different line from second file is: \n\n",g_line1)
                        break
                    #Read the next line from the file
                    f_line1 = f.readline()
                    g_line1 = g.readline()
        break
    else:
        if not (path.exists(x)):
            print("the file "+str(x)+" does not exit!!")
            n=input("Create a file or not? enter 'Y' for yes or 'N' for no: ")

            if(n=="y" or n=="Y"):
                f=open(x,"w")
                f.write(input("Enter the text for the file: "))
                print("Content of file one is ")
                f=open(x,"r")
                print(f.read())
            elif (n=="n" or n=="N"):
                x=input("enter a new file name: ")
                if x[-4:]!=".txt":
                    x+=".txt"
            else:
                print("BYE!!!!")
                quit()
        if not (path.exists(y)):
            print("the file "+str(y)+" does not exit!!")
            n=input("Create a file or not? enter 'Y' for yes or 'N' for no: ")
            if(n=="y" or n=="Y"):
                f=open(y,"w")
                f.write(input("Enter the text for the file: "))
                print("Content of file two is ")
                f=open(y,"r")
                print(f.read())
            elif (n=="n" or n=="N"):
                y=input("enter a new file name: ")
                if y[-4:]!=".txt":
                    y+=".txt"
            else:
                print("BYE!!!!")
                quit()
