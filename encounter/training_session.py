# ------------------------------------------------------------------------
#
#  Function: training_session
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: If the player is a Knight, they gain more health from 
#    training.  Otherwise, they gain a smaller health boost.
#
#  Author: <Maksym Kholodenko>
#
# ------------------------------------------------------------------------

import random

def training_session(health, title):

    if title.lower() == "knight":
        gain = random.randint(8, 12)
        print("As a Knight, your training is intense and effective.")
    else:
        gain = random.randint(3, 6)
        print("You complete a basic training session.")

    print(f"You gain {gain} health.")

    health += gain
    return health
