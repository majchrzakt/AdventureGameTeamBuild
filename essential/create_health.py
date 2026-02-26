"""
Function: create_health
Description: Creates a random initial health value between 50 and 150.
Author: Tom
"""

from random import randint
def create_health() -> int:
    health = randint(50, 150)
    if health < 75:
        print(f"You feel weak, with only {health} health.")
    elif health <= 100:
        print(f"You feel moderately strong, with {health} health.")
    elif health <= 125:
        print(f"You feel as strong as an ox, with {health} health.")
    else:
        print(f"You feel unstoppable, with {health} health!")
    return health