# ------------------------------------------------------------------------
#
#  Function: hidden_trap
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player discovers a hidden trap that reduces health.
#
#  Author: <Maksym Kholodenko>
#
# ------------------------------------------------------------------------

import random

def hidden_trap(health):

    damage = random.randint(2, 6)

    print("You step on a hidden trap!")
    print(f"You take {damage} damage.")

    health -= damage

    if health < 0:
        health = 0

    return health
