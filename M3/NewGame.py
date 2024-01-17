def get_player_name(player_name):
    messages = []

    while True:
        name_input = input(f"Set your name ({player_name})? ")

        if not name_input:  # En caso de que el jugador no ponga nada le dejaremos "Link" por defecto
            return messages, "Link"

        if name_input.lower() == "back":
            messages.append("Going back to the Main menu...")
            return messages, None

        if name_input.isalnum() or name_input.isspace():
            messages.append(f"Welcome to the game, {name_input}!")
            return messages, name_input
        else:
            messages.append(f"{name_input} is not a valid name. Name must be alphanumeric and can contain spaces.")

def new_game_menu(player_name):
    messages = []

    new_game_menu_text = f"""
    * New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    *                                                                             *
    *                                                                             *
    *                                                                             *
    *                                                                             *
    *       Set your name ({player_name})?                                        *
    *                                                                             *
    *                                                                             *
    *                                                                             *
    *       Type 'back' now to go back to the 'Main menu'                         *
    *                                                                             *
    *                                                                             *
    * Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    """

    messages.append(new_game_menu_text)
    result, name_input = get_player_name(player_name)
    messages.extend(result)  # Extiende la lista de mensajes

    return messages




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