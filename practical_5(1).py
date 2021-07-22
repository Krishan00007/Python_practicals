"""
Write a program that computes and prints the average of the numbers in a text file. You should make use 
of two higher-order functions to simplify the design.
"""
def getNumberList(filename):
    f=open(filename,'r')
    strli=f.read().split(',')
    numli=[int(num) for num in strli]
    return numli

def getAverage(filename,func):
    numbers=func(filename)
    return  sum(numbers)/len(numbers)

def main():
    x=input("Enter filename: ")
    if x[-4:]!=".txt":
      x+=".txt"
    average=getAverage(x,getNumberList)
    print("%0.2f" %average)

if __name__=="__main__":
    main()
