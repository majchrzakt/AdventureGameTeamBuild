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
#  Authors: Main program flow created by Tina Majchrzak, February 2026.
#    Individual functions written by students in 161P.
#
# ------------------------------------------------------------------------

import random
import os

# ------------------------------------------------------------------------
# Essential Functions
# ------------------------------------------------------------------------
from essential.create_health import create_health       # by Tom
from essential.create_gold import create_gold           # by Nate
from essential.choose_title import choose_title         # by Lu
from essential.validate_choice import validate_choice   # by B
from essential.status_report import status_report       # by Calli

# ------------------------------------------------------------------------
# Reputation Functions
# ------------------------------------------------------------------------

from reputation.knight_promotion import knight_promotion 
from reputation.secret_path import secret_path           # by Kate
from reputation.lost_map import lost_map
from reputation.magical_training import magical_training # by Jackson
from reputation.royal_favor import royal_favor
from reputation.secret_talisman import secret_talisman

# ------------------------------------------------------------------------
# Encounter Functions
# ------------------------------------------------------------------------

from encounter.forest_attack import forest_attack        # by John Michael
from encounter.river_crossing import river_crossing
from encounter.mystical_potion import mystical_potion
from encounter.hidden_trap import hidden_trap            # by Trevor
from encounter.rest_inn import rest_inn                  # by Carson
from encounter.training_session import training_session  # by Maksym
from encounter.haunted_forest import haunted_forest
from encounter.hidden_pond import hidden_pond            # by Luther
from encounter.ambush import ambush                      # by Coda
from encounter.healing_herbs import healing_herbs        # by Tory

# ------------------------------------------------------------------------
# Wealth Functions
# ------------------------------------------------------------------------

from wealth.find_treasure import find_treasure          # by Torin
from wealth.bandit_ambush import bandit_ambush
from wealth.merchant_sale import merchant_sale
from wealth.find_gem import find_gem                    # by Dario
from wealth.duel_knight import duel_knight
from wealth.gold_mine import gold_mine                  # by Josh
from wealth.cursed_coin import cursed_coin
from wealth.treasure_map import treasure_map
from wealth.lottery import lottery                      # by Alex


# ------------------------------------------------------------------------
# MAIN GAME
# ------------------------------------------------------------------------

def main():
    # --- Clear screen ---
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Adventure Game!\n")

    # --- Set up initial stats ---
    health = create_health()
    gold = create_gold()
    title = choose_title()

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
            rep_choice = random.randint(1, 6)

            if rep_choice == 1:
               title = knight_promotion(title)

            elif rep_choice == 2:
               title = secret_path(title)

            elif rep_choice == 3:
               title = lost_map(title)

            elif rep_choice == 4:
               title = magical_training(title)

            elif rep_choice == 5:
               title = royal_favor(title)

            else:
               title = secret_talisman(title)


        # --- Encounter ---
        elif choice == "2":
            encounter_choice = random.randint(1, 10)

            if encounter_choice == 1:
               health = rest_inn(health, gold)

            elif encounter_choice == 2:
               health = training_session(health, title)

            elif encounter_choice == 3:
               health = forest_attack(health)

            elif encounter_choice == 4:
               health = river_crossing(health)

            elif encounter_choice == 5: 
               health = mystical_potion(health)

            elif encounter_choice == 6:
               health = hidden_trap(health)

            elif encounter_choice == 7:
               health = haunted_forest(health)

            elif encounter_choice == 8:
               health = hidden_pond(health)

            elif encounter_choice == 9:
               health = ambush(health)

            else:
               health = healing_herbs(health)


        # --- Wealth ---
        elif choice == "3":
            gold_choice = random.randint(1, 9)

            if gold_choice == 1:
               gold = find_treasure(gold)

            elif gold_choice == 2:
               gold = bandit_ambush(gold)

            elif gold_choice == 3:
               gold = merchant_sale(gold)

            elif gold_choice == 4:
               gold = find_gem(gold)

            elif gold_choice == 5:
               gold = duel_knight(gold)

            elif gold_choice == 6:
               gold = gold_mine(gold)

            elif gold_choice == 7:
               gold = cursed_coin(gold)

            elif gold_choice == 8:
               gold = treasure_map(gold)

            else:
               gold = lottery(gold)


        # --- Quit ---
        else:
            print("Thanks for playing!")
            game_active = False

if __name__ == "__main__":
    main()

