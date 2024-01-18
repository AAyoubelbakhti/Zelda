from FuncionesPrompt import drawPrompt, addToPrompt
from MenusVisuales import legend, plot
from otrasfunciones import clear_screen
from diccionarios import inventory
from FuncionesHelp import help_new_game


player_name = "Link"


def new_game_menu():
    global player_name
    clear_screen()
    print(f"""
* New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*           Set your name {player_name}                                            *
*                                                                             *
*                                                                             *
*                                                                             *
*       Type 'back' now to go back to the 'Main menu'                         *
*                                                                             *
*                                                                             *
* Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")
    drawPrompt()


    player_name = input("Set your name (Link)? ")
    addToPrompt(player_name)

    if not player_name:  
        inventory["name"] = "Link"
        print("Defaulting to 'Link'.")

    if player_name.lower == "help":
        help_new_game()
        player_name = input()
        addToPrompt(player_name)
        if player_name == "back":
            new_game_menu()

    elif player_name.isalnum() or player_name.isspace():
        inventory["name"] = player_name
        print(f"Welcome to the game, {player_name}!")

    user_input = input("Type 'continue' to continue: ").lower()
    addToPrompt(user_input)

    if user_input == "continue":
        print("Loading...")
        legend()