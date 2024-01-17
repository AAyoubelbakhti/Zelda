def legend():
    messages = []

    legend_menu_text = """
* Legend  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*    10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah  *
*    tribe. The Sheikah were a tribe of warriors who protected the Triforce,  *
*    a sacred relic that granted wishes.                                      *
*                                                                             *
*    But one day, Ganondorf, an evil sorcerer, stole the Triforce and began   *
*    to rule Hyrule with an iron fist.                                        *
*                                                                             *
*    The princess, with the help of a heroic young man, managed to defeat     *
*    Ganondorf and recover the Triforce.                                      *
*                                                                             *
* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
"""

    messages.append(legend_menu_text)
    user_input = input("Type 'continue' to continue: ").lower()


    if user_input == "continue":
        messages.append("Loading...")
    else:
        messages.append("Invalid action. Type 'back' to retunr to the game.")

    return messages


def plot(player_name):
    messages = []

    plot_menu_text = f"""
* Plot  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*  Now history is repeating itself, and Princess Zelda has been captured by   *
*  Ganon. He has taken over the Guardians and filled Hyrule with monsters.    *
*                                                                             *
*                                                                             *
*  But a young man named '{player_name}' has just awakened and                *
*  must reclaim the Guardians to defeat Ganon and save Hyrule.                *
*                                                                             *
*                                                                             *
* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

    messages.append(plot_menu_text)
    user_input = input("Type 'continue' to continue: ").lower()


    if user_input == "continue":
        messages.append("Loading...")
    else:
        messages.append("Invalid action. Type 'back' to retunr to the game.")

    return messages