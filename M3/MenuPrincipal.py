import mysql.connector
from MenuAleatorio import generar_menu_aleatorio
from FuncionesHelp import help_new_game, inventory_help, saved_games_help, main_menu_help
from NewGame import new_game_menu, legend, plot



cnx = mysql.connector.connect(user='root', password='superlocal', host='127.0.0.1', database='ZeldaSQL')

in_new_game = False 
in_inventory = False
in_saved_games = False
in_main_menu = False

player_name = "Link"
prompt = [""] * 8


def clear_prompt():
    global prompt
    prompt = [""] * 8

def add_to_prompt(messages):
    global prompt
    for message in messages:
        if isinstance(message, str):
            prompt.append(message)
        else:
            add_to_prompt(message)

def draw_prompt():
    global prompt
    print('\n'.join(prompt))




def process_action(action):
    global prompt, player_name, in_new_game, in_legend, in_plot, in_inventory, in_main_menu, in_saved_games

    action = action.lower()

    if in_new_game:
        # Lógica específica para el estado 'in_new_game'
        if action == 'continue':
            add_to_prompt("Starting the game...")
            in_legend = True
        elif action == 'back':
            add_to_prompt("Going back to the Main menu...")
            in_new_game = False
        else:
            add_to_prompt("Invalid action. Type 'continue' to start the game.")
    elif in_legend:
        # Lógica específica para el estado 'in_legend'
        if action == 'continue':
            add_to_prompt("Continuing the game...")
            in_plot = True
        elif action == 'back':
            add_to_prompt("Going back to the Main menu...")
            in_legend = False
        else:
            add_to_prompt("Invalid action. Type 'continue' to continue the game.")
    else:
        # Resto de la lógica para otros estados
        if action == 'continue':
            add_to_prompt("Continuing the game...")
        elif action == 'new game':
            add_to_prompt("Starting a new game...")
            in_new_game = True  # Cambia el estado a 'in_new_game'
            new_game_result = new_game_menu(player_name)
            add_to_prompt(new_game_result)

            if new_game_result[-1] == "Welcome to the game!":
                in_new_game = False
                in_legend = True
        elif action == 'help':
            add_to_prompt(main_menu_help())
        elif action == 'about':
            add_to_prompt("About...")
        elif action == 'exit':
            add_to_prompt("Exiting the game. Goodbye!")
            return True  # Indica que el usuario quiere salir del bucle
        else:
            add_to_prompt("Invalid action.")

    return False  # Indica que el bucle debe continuar


def main():
    global in_new_game, in_legend, in_plot
    in_new_game = False
    in_legend = False
    in_plot = False

    while True:
        # Lógica para mostrar el menú principal
        if not (in_new_game or in_legend or in_plot):
            add_to_prompt(generar_menu_aleatorio())
            draw_prompt()
            user_input = input("Enter an action: ").lower()

            if process_action(user_input):
                break
            elif user_input == 'new game':
                in_new_game = True
                new_game_result = new_game_menu(player_name)
                add_to_prompt(new_game_result)

                if new_game_result[-1] == "Welcome to the game!":
                    in_new_game = False
                    in_legend = True

        # Lógica específica para el estado 'in_legend'
        elif in_legend:
            add_to_prompt(legend())
            in_legend = False  # Cambia el estado después de procesar la acción

        # Lógica específica para el estado 'in_plot'
        elif in_plot:
            add_to_prompt(plot(player_name))
            in_plot = False  # Cambia el estado después de procesar la acción


main()





