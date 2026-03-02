# ------------------------------------------------------------------------
#
#  Function: ambush
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player is ambushed and loses health.
#
#  Author: Dakota Roth
#
# ------------------------------------------------------------------------

import random
import time

def ambush(health):
    roll = random.randint(0,4)

    encounter_options = ["a Bear", "a Landslide", "A Storm", "the Knights of Ni", "a Pack of Cute Puppies"]

    print(f"You have been ambushed by {encounter_options[roll]}!")
    time.sleep(1.5)
    if roll == 0:
        # Bear
        hurt = random.randint(1,5)
        print("You fight valantly, and defeat the bear.")
        print("But all victorys have a price, and you took quite a beating.")
        print(f"You took {hurt} damage")
        return health - hurt
    elif roll == 1:
        # Landslide
        print("It strikes you down!")
        print("Tis but a scratch, as you only take 1 damage")
        return health - 1
    elif roll == 2:
        # Storm
        chance = random.randint(1,100)
        print("It rolls over the horizon, thundering down")

        if chance == 100:
            print("BAM!! You are struck by lightning, igniting into flame!")
            print(f"You take {health} points of damage.")
            return 0 # death, health - health should always be 0.
        else:
            print("The rain is wet, but you survive.")
            return health
    elif roll == 3:
        # Knights of Ni
        damage = random.randint(1,4)
        
        print("They demand a shurbbery, but you cannot provide.")
        print(f"They are displeased.")

        # Fun little Ni Sequence
        for i in range(5,1,-1):
            time.sleep(i) # sleep 5, 4, 3, 2, 1
            print("Ni")
        print("NI")
        time.sleep(0.5)

        print(f"You manage to bareley escape with your life, taking {damage} damage")
        return health - damage
    else:
        # Puppies
        print("They are soft and adorable. You pause your journey to pet them.")
        print("Feeling refreshed, you continue on your way.")
        return health

