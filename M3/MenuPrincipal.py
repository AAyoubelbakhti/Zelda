import mysql.connector
from MenuAleatorio import generar_menu_aleatorio
from FuncionesHelp import help_new_game, inventory_help, saved_games_help, main_menu_help, about
from NewGame import new_game_menu, legend, plot
from FuncionesPrompt import clear_prompt, add_to_prompt, draw_prompt
from otrasfunciones import clear_screen




cnx = mysql.connector.connect(user='root', password='superlocal', host='127.0.0.1', database='ZeldaSQL')

in_new_game = False 
in_inventory = False
in_saved_games = False
in_main_menu = False
in_plot = False
in_legend = False


prompt = [""] * 8
player_name = "Link"


# ...

# ...

def main():
    global in_new_game, in_legend, in_plot, in_main_menu, player_name

    while True:
        if in_main_menu:
            # Llama a la función para generar un menú aleatorio
            menu_messages = generar_menu_aleatorio()
            add_to_prompt(menu_messages)

            draw_prompt()
            action = input("Select an option: ").lower()

            clear_screen()  # Limpia la pantalla antes de mostrar el nuevo menú

            if action == 'new game':
                in_main_menu = False
                in_new_game = True
                new_game_result = new_game_menu()
                add_to_prompt(new_game_result)
                if new_game_result and new_game_result[-1] == "Welcome to the game!":
                    in_new_game = False
                    in_legend = True
            elif action == 'continue':
                # Lógica para continuar el juego
                pass
            elif action == 'help':
                add_to_prompt(main_menu_help())
            elif action == 'about':
                add_to_prompt(about())
            elif action == 'exit':
                add_to_prompt("Exiting the game. Goodbye!")
                break
            else:
                add_to_prompt("Invalid action.")
        elif in_new_game:
            # Lógica para el menú de nuevo juego
            new_game_messages = new_game_menu()
            add_to_prompt(new_game_messages)
        elif in_legend:
            # Lógica para el menú de leyenda
            legend_messages = legend(player_name)
            add_to_prompt(legend_messages)
            # Puedes agregar más lógica aquí si es necesario

if __name__ == "__main__":
    main()




