from FuncionesPrompt import draw_prompt
from MenusVisuales import legend, plot
# ...

def new_game_menu():
    messages = []

    new_game_menu_text = f"""
* New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*           Set your name                                                          *
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
        elif player_name.isalnum() or player_name.isspace():
            messages.append(f"Welcome to the game, {player_name}!")

            user_input = input("Type 'continue' to continue: ").lower()

            if user_input == "continue":
                messages.append("Continuing to the plot...")
                # Aquí puedes llamar a la función 'plot_menu' o realizar las acciones necesarias para el menú de 'plot'
                plot_messages = plot(player_name)
                messages.extend(plot_messages)
                return messages, player_name
            else:
                messages.append("Invalid action. Starting a new game.")
                draw_prompt()  # Vuelve a dibujar el prompt para mantener la presentación
        else:
            messages.append(f"{player_name} is not a valid name. Name must be alphanumeric and can contain spaces.")
            draw_prompt()  # Vuelve a dibujar el prompt para mantener la presentación





