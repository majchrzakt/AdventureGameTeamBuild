# ------------------------------------------------------------------------
#
#  Function: secret_path
#
#  Inputs: title (string)
#  Returns: title (string)
#
#  Description: Player discovers a secret path but title stays the same.
#
#  Author: <Kate Bartu>
#
# ------------------------------------------------------------------------

import random

def secret_path(title):
    messages = [
        "You find a path that definitely wasn't here 5 seconds ago."
        "A suspiciously convenient shortcut appears. no questions asked."
        "You found a developer shortcut! pls don't tell the other players..."
        "You found a secret route! {ACHIEVEMENT UNCLOCKED}---|Professional Wanderer|"
        "You discover a secret path! The trees pretend they didn't see anything."
        "You find a hidden path. It smells faintly like plot progression.",
        "You discover a secret trail! The main road looks offended.",
        "A shortcut appears, clearly placed here by a very helpful game designer.",
        "You found the scenic route’s cooler, faster cousin.",
    ]

    print("\nSecret Path")
    print(random.choice(messages))
    return title