"""
A bit shift is a procedure whereby the bits in a bit string are moved to the left or to the right. 
For example, we can shift the bits in the string 1011 two places to the left to produce the string 1110. 
Note that the leftmost two bits are wrapped around to the right side of the string in this operation. 
Define two scripts, shiftLeft.py and shiftRight.py, that expect a bit string as an input. 
The script shiftLeft shifts the bits in its input one place to the left, wrapping the leftmost 
bitto the rightmost position. The script shiftRight performs the inverse operation. Each script 
prints the resulting string.
"""
val = int(input("Enter 1 for Leftshift , 2 for Rightshift:"))
if(val==1):
    num=input("Enter the number you want to left shift: ")
    n=input("enter number of digits you want to shift: ")
    while True:
        if not (num.isnumeric() and n.isnumeric()):
            if not num.isnumeric():
                num=input("Sorry!! Enter a correct number: ")
            else: 
                n=input("Sorry!! Enter number of digits: ")
        else:
            num=int(num)
            n=int(n)
            binary=bin(num)
            print("The binary equivalent of the number is: ",binary)
            leftShift=num<<n
            print("the binary equivalent of the resultant is: ",bin(leftShift))
            print("and the dedial equivalent is: ",leftShift)
            break

elif(val==2):
    num=input("Enter the number you want to right shift: ")
    n=input("enter number of digits you want to shift: ")
    while True:
        if not (num.isnumeric() and n.isnumeric()):
            if not num.isnumeric():
                num=input("Sorry!! Enter a correct number: ")
            else: 
                n=input("Sorry!! Enter number of digits: ")
        else:
            num=int(num)
            n=int(n)
            binary=bin(num)
            print("The binary equivalent of the number is: ",binary)
            rightShift=num>>n
            print("the binary equivalent of the resultant is: ",bin(rightShift))
            print("and the dedial equivalent is: ",rightShift)
            break

else :
    print("Enter a valid value!")