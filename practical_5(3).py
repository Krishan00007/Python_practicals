"""
A list is sorted in ascending order if it is empty or each item except the last one is less than or 
equal to its successor. Define a predicate isSorted that expects a list as an argument and returns 
True if the list is sorted, or returns False otherwise. (Hint: For a list of length 2 or greater, loop 
through the list and compare pairs of items, from left to right, and return False if the first item in 
a pair is greater.)
"""
def issorted(li,n):
    if n == 0:
        return True
    for i in range(n-1):
        if(li[i]>li[i+1]):
            return False
    return True

li=[]
n = int(input("Enter number of elements : "))
li = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print(issorted(li,n))
