import mysql.connector
from MenuAleatorio import generar_menu_aleatorio
from FuncionesHelp import help_new_game, inventory_help, saved_games_help, main_menu_help, about
from NewGame import new_game_menu, player_name
from FuncionesPrompt import addToPrompt,clearPrompt,drawPrompt, prompt
from otrasfunciones import clear_screen




cnx = mysql.connector.connect(user='root', password='superlocal', host='127.0.0.1', database='ZeldaSQL')









def main():
    generar_menu_aleatorio()
    while True:
        user_input = input()
        addToPrompt(user_input)
        if user_input == "new game":
            new_game_menu()
            if player_name.lower() == "back":
                main()
        elif user_input == "continue":
            # Agrega aquí la lógica para continuar el juego
            pass
        elif user_input == "help":
            main_menu_help()
            user_input = input()
            addToPrompt(user_input)
            if user_input == "back":
                main()
            else:
                print("Invalid action, type 'back' to go back to the Main menu")

if __name__ == "__main__":
    main()
