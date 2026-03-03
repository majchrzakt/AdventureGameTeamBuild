# ------------------------------------------------------------------------
#
#  Function: create_gold
#
#  Inputs: none
#  Returns: gold (int)
#
#  Description: Randomly generates starting gold between 0 and 50.
#    Prints a message about starting amount of gold.
#
#  Author: Nathan Muldowney
#
#
# ------------------------------------------------------------------------




import random
#Creates a random amount of gold between 1 and 50.
#Prints the starting amount of gold, and returns gold
def create_gold():
    gold = random.randint(0, 50)
    print(f"You start the game with {gold} gold.")
    return gold