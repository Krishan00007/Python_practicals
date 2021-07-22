"""
Define a function decimalToRep that returns the representation of an integer in a given base. The two 
arguments should be the integer and the base. The function should return a string. It should use a lookup 
table that associates integers with digits. Include a main function that tests the conversion function 
with numbers in several bases.
"""
def decimalToRep(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else :
        return decimalToRep(n//base,base) + convertString[n%base]
if __name__ == '__main__':
    print(decimalToRep(1453,2))
    print(decimalToRep(1453,3))
    print(decimalToRep(1453,8))
    print(decimalToRep(1453,16))
    print(decimalToRep(7,10))
    print(decimalToRep(2,4))
