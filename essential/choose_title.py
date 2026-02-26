# ------------------------------------------------------------------------
#
#  Function: choose_title
# 
#  Inputs: none
#  Returns: title (string)
#
#  Description: Randomly selects a starting title (like Wanderer or 
#    Apprentice) and prints it.
#
#  Author: Chenglu
#
# ------------------------------------------------------------------------

import random

def choose_title():
    titles = ["Wanderer", "Apprentice", "Knight", "Mage", "Rogue"]
    title = random.choice(titles)
    print("Your starting title is:", title)
    return title

