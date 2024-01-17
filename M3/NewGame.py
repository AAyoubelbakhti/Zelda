from FuncionesPrompt import draw_prompt
def new_game_menu():
    messages = []
    player_name = "Link"
    new_game_menu_text = f"""
* New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*           Set your name {player_name}                                                *
*                                                                             *
*                                                                             *
*                                                                             *
*       Type 'back' now to go back to the 'Main menu'                         *
*                                                                             *
*                                                                             *
* Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

    messages.append(new_game_menu_text)
    draw_prompt()

    while True:
        player_name = input("Set your name (Link)? ")

        if not player_name:  
            player_name = "Link"
            messages.append("Defaulting to 'Link'.")

        if player_name.lower() == "back":
            messages.append("Going back to the Main menu...")
            return messages, None

        if player_name.isalnum() or player_name.isspace():
            messages.append(f"Welcome to the game, {player_name}!")
            return messages, player_name
        else:
            messages.append(f"{player_name} is not a valid name. Name must be alphanumeric and can contain spaces.")
            draw_prompt()  # Vuelve a dibujar el prompt para mantener la presentación





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