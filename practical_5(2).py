"""
Define and test a function myRange. This function should behave like Python’s standard range function, 
with the required and optional arguments, but it should return a list. Do not use the range function in 
your implementation! (Hints: Study Python’s help on range to determine the names, positions, and what to 
do with your function’s parameters. Use a default value of None for the two optional parameters. If these 
parameters both equal None, then the function has been called with just the stop value. If just the third 
parameter equals None, then the function has been called with a start value as well. Thus, the first part 
of the function’s code establishes what the values of the parameters are or should be. The rest of the 
code uses those values to build a list by counting up or down.)
"""
def myRange(*args):
    li=[]
    if len(args) == 1:
        k=0
        if args[0]>0:
            while k<args[0]:
                li.append(k)
                k+=1
        else:
            li=[]
    elif(len(args) == 2):
        k=args[0]
        if args[0]<args[1]:
            while k<args[1]:
                li.append(k)
                k+=1
        else:
            k=args[1]
            while k<args[0]:
                li.append(k)
                k+=1
            # li=li.reverse()
    elif(len(args) == 3):
        k=args[0]
        if args[0]<args[1]:
            while k<args[1]:
                li.append(k)
                k+=args[2]
        else:
            k=args[1]
            while k<args[0]:
                li.append(k)
                k+=args[2]
    else:
        li=[]
        print("Enter three inputs")
    return li

li=myRange(2,10)
print(li)
