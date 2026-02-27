# Function: status_report
#
#  Inputs: health (int), gold (int), title (string)
#  Returns: none
#
#  Description: Displays the player’s current health, gold, and title
#    in a format that's easy to read quickly.
#
#  Author: <CalliGilbertNeel>
#
# ------------------------------------------------------------------------
def status_report(health, gold, title):
    if health >= 80:
        health_status = "You're Unstoppable!"
    elif health >= 45:
        health_status = "Hang in there!"
    else:
        health_status = "Uh Oh!"

    print(f"Title; {title}, Health: {health}, Gold: {gold}, Status {health_status}")

