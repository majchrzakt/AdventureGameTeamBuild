# ------------------------------------------------------------------------
#
#  Program: Adventure Game
#
#  Description: This program is a simple adventure game where the player 
#    chooses between advancing their reputation, facing an encounter, 
#    or increasing their wealth.  After making one of these choices, a 
#    random scenario plays out.  The player can continue choosing between 
#    these three options or can choose to quit.
#
#  Author: Main program flow created by Tina Majchrzak with assitance
#    from ChatGPT (OpenAI), February 2026.  Individual functions written 
#    by students in 161P.
#
# ------------------------------------------------------------------------

import random
import os

# ----------------------------------------------------------
# Essential Functions
# ----------------------------------------------------------
from essential.create_health import create_health       # by Tom
from essential.create_gold import create_gold           # by Nate
from essential.choose_title import choose_title         # by Lu
from essential.validate_choice import validate_choice   # by B
from essential.status_report import status_report       # by Calli

# ----------------------------------------------------------
# Reputation Functions
# ----------------------------------------------------------

from reputation.knight_promotion import knight_promotion 
from reputation.secret_path import secret_path           # by Kate
from reputation.lost_map import lost_map
from reputation.magical_training import magical_training
from reputation.royal_favor import royal_favor
from reputation.secret_talisman import secret_talisman

# ----------------------------------------------------------
# Encounter Functions
# ----------------------------------------------------------

from encounter.forest_attack import forest_attack        # by John Michael
from encounter.river_crossing import river_crossing
from encounter.mystical_potion import mystical_potion
from encounter.hidden_trap import hidden_trap
from encounter.rest_inn import rest_inn                  # by Carson
from encounter.training_session import training_session
from encounter.haunted_forest import haunted_forest
from encounter.hidden_pond import hidden_pond
from encounter.ambush import ambush
from encounter.healing_herbs import healing_herbs

# ----------------------------------------------------------
# Wealth Functions
# ----------------------------------------------------------

from wealth.find_treasure import find_treasure
from wealth.bandit_ambush import bandit_ambush
from wealth.merchant_sale import merchant_sale
from wealth.find_gem import find_gem             # by Dario
from wealth.duel_knight import duel_knight
from wealth.gold_mine import gold_mine
from wealth.cursed_coin import cursed_coin
from wealth.treasure_map import treasure_map
from wealth.lottery import lottery               # by Alex


# ----------------------
# MAIN GAME
# ----------------------

def main():
    # --- Clear screen ---
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Adventure Game!\n")

    # --- Set up initial stats ---
    health = create_health()
    gold = create_gold()
    title = choose_title()

    # --- Function lists in reputation, encounter, and wealth categories ---
    title_functions = [
        knight_promotion, secret_path, lost_map,
        magical_training, royal_favor, secret_talisman
    ]
    health_functions = [
        forest_attack, river_crossing, mystical_potion, hidden_trap,
        rest_inn, training_session, haunted_forest, hidden_pond,
        ambush, healing_herbs
    ]
    gold_functions = [
        find_treasure, bandit_ambush, merchant_sale, find_gem,
        duel_knight, gold_mine, cursed_coin, treasure_map, lottery
    ]

    # --- Game loop ---
    game_active = True
    while game_active:
        # --- Display stats ---
        print()
        status_report(health, gold, title)

        # --- Display menu ---
        print()
        print("Choose what to do:")
        print("1 - Advance Reputation")
        print("2 - Face Encounter")
        print("3 - Increase Wealth")
        print("4 - Quit")

        # --- Get user choice ---
        print()
        choice = validate_choice("Enter 1, 2, 3, or 4: ", ["1","2","3","4"])

        # --- Clear screen ---
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("The adventure continues!\n")

        # --- Run random scenario from chosen category ---
        # --- Reputation ---
        if choice == "1":
            func = random.choice(title_functions)
            title = func(title)

        # --- Encounter: functions require 1 OR 2 arguments ---
        elif choice == "2":
            func = random.choice(health_functions)
            if func.__name__ in ["rest_inn"]:
                health = func(health, gold)
            elif func.__name__ in ["rest_inn", "training_session"]:
                health = func(health, title)
            else:
                health = func(health)

        # --- Wealth ---
        elif choice == "3":
            func = random.choice(gold_functions)
            gold = func(gold)

        # --- Quit ---
        else:
            print("Thanks for playing!")
            game_active = False

if __name__ == "__main__":
    main()

