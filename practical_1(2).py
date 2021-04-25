"""
Write a program that takes the radius of a sphere (a floating-point number) as
input and then outputs the sphere’s diameter, circumference, surface area, and volume.
"""
from math import pi
radius=float(input("Enter a number :"))
diameter=round((2.0*radius),3)
circumfrence=round((2.0*pi*radius),3)
surface_area=round((4.0*pi*radius),3)
volume=round(((4.0/3.0)*(pi*(radius**3))),3)
print("Diameter of sphere :",diameter)
print("Circumfrence of sphere :",circumfrence)
print("Surface area of sphere",surface_area)
print("Volume of sphere :",volume)
input("Press any key to exit")