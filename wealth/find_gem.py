# ------------------------------------------------------------------------
#
#  Function: find_gem
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player finds a gem worth a random amount of gold.
#
#  Author: <Dario Lopez>
#
# ------------------------------------------------------------------------

import random

def find_gem(gold):
    #Generate a random interger between 1 and 20
    new_gold = random.randint(1, 20)
    # Print the result
    print(f"You found a gem worth {new_gold} gold!")
    return gold + new_gold
