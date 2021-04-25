"""
Write a program that accepts the lengths of three sides of a triangle as inputs. The
program output should indicate whether or not the triangle is a right triangle. Recall from
the Pythagorean theorem that in a right triangle, the square of one side equals the sum of
the squares of the other two sides.
"""
x=int(input("Enter value of first side of triangle :"))
y=int(input("Enter value of second side of triangle :"))
z=int(input("Enter value of third side of triangle :"))
hyp=0
height=0
len=0

#check user input conditions
if((x>y) and (x>z)):
    hyp=x
if((y>x) and (y>z)):
    hyp=y
if((z>x) and (z>y)):
    hyp=z

if(hyp==x):
    height=y
    len=z
elif(hyp==y):
    height=z
    len=x
else:
    height=x
    len=y

#calculation of right triangle
hyp=hyp**2
sum_of_sides=(height**2) + (len**2)

#check for right triangle
if(hyp==sum_of_sides):
    print("The given triangle is right triangle")
else:
    print("The given triangle is not right triangle")



