# ------------------------------------------------------------------------
#
#  Function: find_treasure
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player finds treasure and gains a random amount of gold.
#
#  Author: Torin
#
# ------------------------------------------------------------------------

from random import randint

def find_treasure(gold):
    tv = gold + randint(8,29) #tv = total value
    treasure = ["large sapphire","circlet","golden statue","ruby ring", "lost artifact"]
    print(f"In a small crevice, you catch a glimpse of a weary vessel, long\n"
          f"forgotten by time. Reaching in, you find your hand grasping an\n"
          f"old, tired handle. You gasp! It contains a {treasure[randint(0,len(treasure)-1)]} and gold!")
    return tv

find_treasure(5)
