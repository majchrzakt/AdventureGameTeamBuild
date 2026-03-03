# ------------------------------------------------------------------------
#
#  Function: mystical_potion
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Drinking a potion restores a random amount of health.
#
#  Author: <Maksym Kholodenko>
#
# ------------------------------------------------------------------------

import random

def mystical_potion(health):

    restore = random.randint(5, 10)

    print("You drink a mystical potion.")
    print(f"It restores {restore} health.")

    health += restore
    return health
