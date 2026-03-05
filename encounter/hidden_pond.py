# ------------------------------------------------------------------------
#
#  Function: hidden_pond
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player discovers a hidden pond that restores health.
#
#  Author: Luther Atchison
#
# ------------------------------------------------------------------------

import random

def hidden_pond(health):
    """
    Player discovers a hidden pond that restores a random amount of health.
    Also randomizes what noise is heard upon initial encounter.
    """

    frogSounds = ["\"Ribbit!\"", "\"Croak!\"", "\"Croak-croak...\"", "\"Crooaakk, crooaaakkk...\"", "\"Crooaaak...?\""]
    # List of sounds that have a chance to be heard when initially encountering hidden pond.
    ribbitSound = frogSounds[random.randint(0,len(frogSounds)-1)]
    # Randomly picks an indexed element from frogSounds.

    addHealth = random.randint(5, 10)
    # Randomly picks the integer amount to add to player's health, between values 5 and 10.

    print(f"{ribbitSound}")
    # Prints the random frog sound.
    print(f"The chirping of frogs steadily enter your ears...? It's a little, hidden pond you seem to have stumbled upon!\nIt looks surprisingly clean, so you decide to clean yourself up a bit in the still liquid, frogs hopping away from your added presence...")
    # Prints encounter dialogue.
    print(f"You feel refreshed and clean... Your health has increased by {addHealth} points!")
    # Prints present encounter dialogue and reports how many points were added to player's health.

    newHealth = health + addHealth
    # Temporary variable containing health by addHealth's randomized amount added to player's health before encounter.

    print(f"Your health is now at {newHealth}!\nYou leave the pond, feeling satisfied, as the sound of croaking dissipates...\n")
    # Prints end-of-encounter dialogue and reports the player's current health value, using newHealth, after it has been increased.

    health = newHealth
    # Actually updates the amount of health the player has after encounter.

    return health
    # Returns the amount of health the player now has after encounter.