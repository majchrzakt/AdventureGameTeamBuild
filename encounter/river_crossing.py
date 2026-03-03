# ------------------------------------------------------------------------
#
#  Function: river_crossing
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player may lose a small amount of health while crossing 
#    a river.
#
#  Author: <Maksym Kholodenko>
#
# ------------------------------------------------------------------------

import random

def river_crossing(health):

    chance = random.randint(1, 2)

    if chance == 1:
        damage = random.randint(1, 4)
        print("You slip while crossing the river.")
        print(f"You lose {damage} health.")
        health -= damage
    else:
        print("You safely cross the river.")

    if health < 0:
        health = 0

    return health
