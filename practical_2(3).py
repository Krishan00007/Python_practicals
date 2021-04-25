"""
In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7, the
player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible, a
casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so on. A little
mathematical analysis reveals that there are not enough ways to win to make the game
worthwhile; however, because many people’s eyes glaze over at the first mention of
mathematics, your challenge is to write a program that demonstrates the futility of
playing the game. Your program should take as input the amount of money that the
player wants to put into the pot, and play the game until the pot is empty. At that point,
the program should print the number of rolls it took to break the player, as well as
maximum amount of money in the pot.
"""
import random
print("Welcome to LUCKY SEVEN GAME")
amount = float(input("Entre total amount of money for game :"))

#logic of game
i=1
list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6]

while 1:
    if(amount>0):
        
            val1 = random.choice(list1)
            val2 = random.choice(list2)
            val3 = val1 + val2
            print("No. comes on", i ,"pass :",val3)
            if(val3==7):
                print("Your are LUCKY ,SEVEN comes, $4 is added your amount")
                amount = amount + 4
            else:
                print("You Loose TRY AGAIN, $1 loose from amount!!")
                amount = amount - 1

            print("Your Current amount :",amount)
            input("\nPrint any key to next pass ;")
            i=i+1
    else:
        break
    
print("Your amount is NULL or Zero")
print("<------------------_Game End_------------------->")

