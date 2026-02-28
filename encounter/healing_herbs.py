# ------------------------------------------------------------------------
#
#  Function: healing_herbs
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player discovers healing herbs that restore a small
#    amount of health.
#
#  Author: Victoria Coleman
#
# ------------------------------------------------------------------------

import random

def healing_herbs(health):
    """
    The player discovers a random healing herb that restores a small amount of
    health.
    """

    #Choose a random herb
    herb = random.randint(1,3)

    if herb == 1:
        print("You find some lavender.\nYou feel much calmer now.")
        #add a random amount of health
        health += random.randint(2, 3)

    elif herb == 2:
        print("You find some peppermint.\nYou're stomach is settled.")
        health += random.randint(3,4)

    else:
        print("You find some aloe.\nIt soothed your skin.")
        health += random.randint(4,5)

    return health

