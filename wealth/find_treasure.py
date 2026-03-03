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
    print("In a small crevice, you catch a glimpse of a weary vessel, long\n"
          "forgotten by time. Reaching in, you find your hand grasping an\n"
          "old, tired handle. You gasp! It's full of gems and curiosities!")
    return tv
