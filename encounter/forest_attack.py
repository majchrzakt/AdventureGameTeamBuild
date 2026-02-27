# ------------------------------------------------------------------------
#
#  Function: forest_attack
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player is attacked by wolves and loses a random amount 
#  of health.
#
#  Author: <John Michael Soza>
#
# ------------------------------------------------------------------------

import random

def forest_attack(health):
    print("Forest Attack!")
    damage = random.randint(0,5)
    print("A feral pack of starving wolves assail you from the bushes!\nThe foremost wolf lunges at you baring it's saliva-imbued fangs!")

    if damage == 0:
        health = health
        print("The wolf missed it's mark! You remain unharmed!")
    else:
        health = health - damage
        print(f"You suffered {damage} points of damage!")

    if health > 0:
        print(f"Your remaining health is {health}")
    else:
        print("The jagged fangs tore into your throat!\nThe wolves gorge themselves on your lifeless corpse.")

    return health
