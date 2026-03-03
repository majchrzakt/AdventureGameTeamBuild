# ------------------------------------------------------------------------
#
#  Function: magical_training
#
#  Inputs: title (string)
#  Returns: title (string)
#
#  Description: Player undergoes magical training and gains a more
#    prestigious title, where "Wise " is added to the front of it.
#
#  Author: Jackson Rodosta
#
# ------------------------------------------------------------------------

import random

def magical_training(title):
    Training = [
        "You are wandering through the woods one day when you stumble upon a crooked shack.\nInside is an old witch who asks for your help with their chores. You eventually agree and spend an hour helping them brew a potion.\nHowever, after you are done they have another task, and another, and another.\nBy the time you are able to escape you feel as though you could recite a dozen of those recipes by heart.",
        "You are enjoying a nice rest when a wizard comes running out of a bush and throws a bag of sparkling dust at you before diving into a river.\nYou cough and sputter as you swat the dust away.\nWhen it clears you begin to feel as though you can sense the laylines of the world. \nThis is probably a good thing... you hope.",
        "It begins to rain suddenly and you run to seek shelter.\nYou find a nice cave, though it seems a wizard has found this place first.\nYou and the wizard wait out the rain and exchange stories of your travels.\nYou turn out to be very good at asking questions, and the wizard seems quite thorough at answering.\nAs you part ways you feel as though you've learned something.",
        "You hear someone calling for help. You rush to their aid and find an old mage stuck ensnared in living vines.\nThrough much effort you are able to free them from their bindings.\nThe mage is so grateful they offer to get you free lessons at their academy.\nEventually your curiosity gets the better of you.\nYou begin attending a few classes at the small schoolhouse when you find the time.\nYou turn out to be a great student, and eventually even earn a small certificate.\nIt seems the certificate is not officially recognized by any guilds.\nYou still treasure the knowledge.",
        "You hear cries from the woods. A small animal seems to be stuck in a trap.\nIn a moment of compassion you set the beast free. The creature turns to run, but hesitates.\nIt looks into your eyes and speaks directly into your mind an ancient secret.\nNow whenever you are alone in the woods, and you listen very closely, you can hear them celebrating their freedom."
    ]

    print(random.choice(Training))
    print("Over time this experience leaves its mark on your legacy.")
    return "Wise " + title
