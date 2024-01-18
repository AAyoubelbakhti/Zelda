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
            return None
        elif player_name.isalnum() or player_name.isspace():
            inventory["name"] = player_name
            print(f"Welcome to the game, {player_name}!")

        user_input = input("Type 'continue' to continue: ").lower()
        addToPrompt(user_input)

        if user_input == "continue":
            print("Loading...")
            legend_messages = legend()
            messages.extend(legend_messages)
            clear_screen()
            draw_prompt()
            

            user_input = input("Type 'continue' to continue: ").lower()

            if user_input == "continue":
                messages.append("Loading...")
                # Aquí puedes llamar a la función 'plot_menu' o realizar las acciones necesarias para el menú de 'plot'
                plot_messages = plot(player_name)
                messages.extend(plot_messages)
                clear_screen()
                draw_prompt()
                return messages, player_name
            else:
                messages.append("Invalid action. Starting a new game.")
                clear_screen()
                draw_prompt()
        else:
            messages.append(f"{player_name} is not a valid name. Name must be alphanumeric and can contain spaces.")
            clear_screen()
            draw_prompt()





