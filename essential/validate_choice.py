# ------------------------------------------------------------------------
#
#  Function: validate_choice
#
#  Inputs: prompt (string), choices (list of valid strings)
#  Returns: valid user choice (string)
#
#  Description: Keeps asking the user for input until they enter one of 
#    the allowed choices. Ensures the menu never crashes.
#
#  Author: B Mbeh
#
# ------------------------------------------------------------------------

def validate_choice(prompt, choices):
    # Use quotes for strings and indentation for the function body
    #print("--- Validate Choice ---")

    while True: # rewrite using best practices (not while True)
        c = input(prompt)
        if c in choices:
            return c
        else:
            print(f"Invalid input. Please choose from: {choices}")
