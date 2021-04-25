"""
A standard science experiment is to drop a ball and see how high it bounces. Once the
“bounciness” of the ball has been determined, the ratio gives a bounciness index. For
example, if a ball dropped from a height of 10 feet bounces 6 feet high, the index is 0.6,
and the total distance traveled by the ball is 16 feet after one bounce. If the ball were to
continue bouncing, the distance after two bounces would be 10 ft + 6 ft + 6 ft + 3.6 ft =
25.6 ft. Note that the distance traveled for each successive bounce is the distance to the
floor plus 0.6 of that distance as the ball comes back up. Write a program that lets the
user enter the initial height from which the ball is dropped and the number of times the
ball is allowed to continue bouncing. Output should be the total distance traveled by the
ball.
"""
#taking inputs
print("From where the ball is droped")
initial_value = float(input("Enter intial height :"))
bounces = int(input("Entre value of NO. of bounces :"))
result=0
index=0.6

for i in range(bounces):
    result = result + initial_value + (initial_value*index)
    initial_value = initial_value*index

print("The Total distance travvelled by ball is :", round(result,2), "ft")