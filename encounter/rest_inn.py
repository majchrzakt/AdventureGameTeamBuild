# ------------------------------------------------------------------------
#
#  Function: rest_inn
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: If the player has enough gold, they pay to rest and gain 
#    a lot of health.  If not, they gain a small amount of health for free.
#
#  Author: <Maksym Kholodenko>
#
# ------------------------------------------------------------------------

import random

def rest_inn(health, gold):

    print("You arrive at a cozy inn.")

    if gold >= 10:
        choice = input("Would you like to pay 10 gold for a full rest? (yes/no): ").strip().lower()

        if choice == "yes":
            print("You enjoy a warm meal and a soft bed.")
            gold -= 10
            health += 15
        else:
            print("You rest near the fireplace instead.")
            health += 5
    else:
        print("You cannot afford a room, so you rest near the fireplace.")
        health += 5

    return health, gold
