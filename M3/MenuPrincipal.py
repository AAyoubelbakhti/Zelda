import mysql.connector
from MenuAleatorio import generar_menu_aleatorio
from FuncionesHelp import help_new_game, inventory_help, saved_games_help, main_menu_help, about
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




def main():
    player_name = "Link"  # Puedes establecer un nombre predeterminado o dejarlo vacío

    # Menú principal
    while True:
        menu_messages = generar_menu_aleatorio()
        add_to_prompt(menu_messages)
        draw_prompt()

        user_input = input("Select an option: ").lower()

        if user_input == "new game":
            clear_prompt()
            new_game_messages = new_game_menu(player_name)
            add_to_prompt(new_game_messages)

            # Puedes agregar más lógica relacionada con el juego aquí

        elif user_input == "continue":
            # Agregar lógica para continuar el juego (si es necesario)
            pass

        elif user_input == "help":
            # Agregar lógica para mostrar la ayuda del juego
            pass

        elif user_input == "about":
            clear_prompt()
            about_messages = about()
            add_to_prompt(about_messages)


        elif user_input == "exit":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()





