"""
Write a script named copyfile.py. This script should prompt the user for the names of two text files. 
The contents of the first file should be input and written to the second file.
"""
import os
x,y=input("Enter names of two text files without .txt extension: ").split()
if x[-4:]!=".txt":
     x+=".txt"
if y[-4:]!=".txt":
    y+=".txt"
f=open(x,"w")
f.write(input("Enter the text: "))
print("Contents of file one i.e. " + x +" : ")
f=open(x,"r")
print(f.read())

f=open(y,"w")
g=open(x,"r")
z=g.read()
f.write(z)
print("Contents of file two i.e. " + y +" : ")
f=open(y,"r")
print(f.read())
f.close()
g.close()
os.remove(x)
os.remove(y)
