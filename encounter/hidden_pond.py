# ------------------------------------------------------------------------
#
#  Function: hidden_pond
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player discovers a hidden pond that restores health.
#
#  Author: <Maksym Kholodenko>
#
# ------------------------------------------------------------------------

import random

def hidden_pond(health):

    restore = random.randint(3, 7)

    print("You discover a hidden pond shimmering in the sunlight.")
    print(f"You feel refreshed and gain {restore} health.")

    health += restore
    return health
