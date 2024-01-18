from FuncionesPrompt import drawPrompt, addToPrompt
from MenusVisuales import legend, plot
from otrasfunciones import clear_screen
from diccionarios import inventory


def new_game_menu():

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

    while True:
        player_name = input("Set your name (Link)? ")
        addToPrompt(player_name)

        if not player_name:  
            inventory["name"] = "Link"
            print("Defaulting to 'Link'.")

        if player_name.lower() == "back":
            print("Going back to the Main menu...")
            main()
        elif player_name.isalnum() or player_name.isspace():
            inventory["name"] = player_name
            print(f"Welcome to the game, {player_name}!")

        user_input = input("Type 'continue' to continue: ").lower()
        addToPrompt(user_input)

        if user_input == "continue":
            print("Loading...")
            legend()