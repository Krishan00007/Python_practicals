# Python_practicals

**Data types, Operators and Expressions: (Do any three projects from the following)
In each of the projects that follow, you should write a program that contains an introductory
docstring. This documentation should describe what the program will do (analysis) and how it
will do it (design the program in the form of a pseudo code algorithm). Include suitable prompts
for all inputs, and label all outputs appropriately. After you have coded a program, be sure to test
it with a reasonable set of legitimate inputs.**

1. The tax calculator program of the case study outputs a floating-point number that might
show more than two digits of precision. Use the round function to modify the program to
display at most two digits of precision in the output number.

2. You can calculate the surface area of a cube if you know the length of an edge. Write a
program that takes the length of an edge (an integer) as input and prints the cube’s
surface area as output.

3. Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to
buy LP record albums. The store rents new videos for $3.00 a night, and oldies for $2.00
a night. Write a program that the clerks at Five Star Retro Video can use to calculate the
total charge for a customer’s video rentals. The program should prompt the user for the
number of each type of video and output the total

4. Write a program that takes the radius of a sphere (a floating-point number) as input and
then outputs the sphere’s diameter, circumference, surface area, and volume.

5. An object’s momentum is its mass multiplied by its velocity. Write a program that
accepts an object’s mass (in kilograms) and velocity (in meters per second) as inputs and
then outputs its momentum.

6. The kinetic energy of a moving object is given by the formula KE = (1 / 2)mv2
where m is the object’s mass and v is its velocity. Modify the program you created in Project 5 so
that it prints the object’s kinetic energy as well as its momentum.

7. Write a program that calculates and prints the number of minutes in a year.
8. Light travels at 3 * 10^8 meters per second. A light-year is the distance a light beam
travels in one year.

9. An employee’s total weekly pay equals the hourly wage multiplied by the total number of
regular hours plus any overtime pay. Overtime pay equals the total overtime hours
multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly
wage, total regular hours, and total overtime hours and displays an employee’s total
weekly pay.

10. Write a program that calculates and displays the value of a light-year. Write a program
that takes as input a number of kilometers and prints the corresponding number of
nautical miles. Use the following approximations:
 A kilometer represents 1/10,000 of the distance between the North Pole and the
equator.
 There are 90 degrees, containing 60 minutes of arc each, between the North Pole and
the equator.
 A nautical mile is 1 minute of an arc.

**Loops and Selection Statements :(Do any three projects from the following)**
1. Write a program that accepts the lengths of three sides of a triangle as inputs. The
program output should indicate whether or not the triangle is an equilateral triangle.

2. Write a program that accepts the lengths of three sides of a triangle as inputs. The
program output should indicate whether or not the triangle is a right triangle. Recall from
the Pythagorean theorem that in a right triangle, the square of one side equals the sum of
the squares of the other two sides.

3. A standard science experiment is to drop a ball and see how high it bounces. Once the
“bounciness” of the ball has been determined, the ratio gives a bounciness index. For
example, if a ball dropped from a height of 10 feet bounces 6 feet high, the index is 0.6,
and the total distance traveled by the ball is 16 feet after one bounce. If the ball were to
continue bouncing, the distance after two bounces would be 10 ft + 6 ft + 6 ft + 3.6 ft =
25.6 ft. Note that the distance traveled for each successive bounce is the distance to the
floor plus 0.6 of that distance as the ball comes back up. Write a program that lets the
user enter the initial height from which the ball is dropped and the number of times the
ball is allowed to continue bouncing. Output should be the total distance traveled by the
ball.

4. A local biologist needs a program to predict population growth. The inputs would be the
initial number of organisms, the rate of growth (a real number greater than 0), the number
of hours it takes to achieve this rate, and a number of hours during which the population
grows. For example, one might start with a population of 500 organisms, a growth rate of
2, and a growth period to achieve this rate of 6 hours. Assuming that none of the
organisms die, this would imply that this population would double in size every 6 hours.
Thus, after allowing 6 hours for growth, we would have 1000 organisms, and after 12
hours, we would have 2000 organisms. Write a program that takes these inputs and
displays a prediction of the total population.

5. The German mathematician Gottfried Leibniz developed the following method to
approximate the value of n: n/4 = 1-1/3 + 1/5-1/7 + ...
Write a program that allows the user to specify the number of iterations use in this
approximation and that displays the resulting value.

6. Teachers in most school districts are paid on a schedule that provides a salary based on
their number of years of teaching experience. For example, a beginning teacher in the
Lexington School District might be paid $30,000 the first year. For each year of
experience after this first year, up to 10 years, the teacher receives a 2% increase over the
preceding value. Write a program that displays a salary schedule, in tabular format, for
teachers in a school district. The inputs are the starting salary, the percentage increase,
and the number of years in the schedule. Each row in the schedule should contain the
year number and the salary for that year.

7. The greatest common divisor of two positive integers, A and B, is the largest number that
can be evenly divided into both of them. Euclid’s algorithm can be used to find the
greatest common divisor (GCD) of two positive integers. You can use this algorithm in
the following manner:
a. Compute the remainder of dividing the larger number by the smaller number.
b. Replace the larger number with the smaller number and the smaller number with the
remainder.
c. Repeat this process until the smaller number is zero.
The larger number at this point is the GCD of A and B. Write a program that lets the user
enter two integers and then prints each step in the process of using the Euclidean
algorithm to find their GCD.

8. Write a program that receives a series of numbers from the user and allows the user to
press the enter key to indicate that he or she is finished providing inputs. After the user
presses the enter key, the program should print the sum of the numbers and their average.

9. The credit plan at TidBit Computer Store specifies a 10% down payment and an annual
interest rate of 12%. Monthly payments are 5% of the listed purchase price, minus the
down payment. Write a program that takes the purchase price as input. The program
should display a table, with appropriate headers, of a payment schedule for the lifetime of
the loan. Each row of the table should contain the following items:
• the month number (beginning with 1)
• the current total balance owed
• the interest owed for that month
• the amount of principal owed for that month
• the payment for that month
• the balance remaining after payment
The amount of interest for a month is equal to balance * rate /12. The amount of principal
for a month is equal to the monthly payment minus the interest owed.

10. In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7, the
player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible, a
casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so on. A little
mathematical analysis reveals that there are not enough ways to win to make the game
worthwhile; however, because many people’s eyes glaze over at the first mention of
mathematics, your challenge is to write a program that demonstrates the futility of
playing the game. Your program should take as input the amount of money that the
player wants to put into the pot, and play the game until the pot is empty. At that point,
the program should print the number of rolls it took to break the player, as well as
maximum amount of money in the pot
