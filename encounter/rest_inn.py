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
#  Author: <Carson Bernardo>
#
# ------------------------------------------------------------------------

REST_COST = 20
MAX_HEALTH = 100
player_gold = 25 

def rest_inn(health):
    global player_gold
    
    print("You enter the warm, dimly lit inn.")
    
    # Check if the player has enough gold
    if player_gold >= REST_COST:
        print(f"You hand the innkeeper {REST_COST} gold and get a comfortable room.")
        player_gold -= REST_COST
        health += 50  # Gain a lot of health, but pay 20 gold
    else:
        print("You don't have enough gold for a room. You huddle in the stables for the night.")
        health += 10  # Gain a small amount of health for free
        
    # Ensure health doesn't exceed the maximum limit
    if health > MAX_HEALTH:
        health = MAX_HEALTH
        
    print(f"You wake up feeling rested. Current health: {health}")
    
    return health
