""""
The kinetic energy of a moving object is given by the formula KE = (1 / 2)mv2
where m is the object’s mass and v is its velocity. Modify the program you created 
in Project :- 
(An object’s momentum is its mass multiplied by its velocity. Write a program that
accepts an object’s mass (in kilograms) and velocity (in meters per second) as inputs and
then outputs its momentum.)
so that it prints the object’s kinetic energy as well as its momentum.
"""
mass_kg = float(input("Enter mass of object(kg) : "))
velocity_mps = float(input("Enter velocity of object(mps) : "))
momentum = round((mass_kg*velocity_mps),3)
kinetic_energy = round((1/2)*mass_kg*(velocity_mps**2))
print("Momentum of object is :",momentum)
print("Kinetic energy of object is :",kinetic_energy)
input("Press any key to exit :")