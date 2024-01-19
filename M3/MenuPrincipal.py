import mysql.connector
from MenuAleatorio import generar_menu_aleatorio
from FuncionesHelp import help_new_game, inventory_help, saved_games_help, main_menu_help, about
from FuncionesPrompt import addToPrompt,clearPrompt,drawPrompt, prompt
from otrasfunciones import clear_screen
from diccionarios import inventory
from MenusVisuales import legend


cnx = mysql.connector.connect(user='root', password='superlocal', host='127.0.0.1', database='ZeldaSQL')






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
*           Set your name {player_name}                                                *
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

    if player_name.lower() == "help":
        help_new_game()
        player_name = input()
        addToPrompt(player_name)
        if player_name.lower() == "back":
            new_game_menu()

    if player_name.lower() == "back":
        main()

    elif not player_name:  
        inventory["name"] = "Link"
        print("Defaulting to 'Link'.")


    elif player_name.isalnum() or player_name.isspace():
        inventory["name"] = player_name
        print(f"Welcome to the game, {player_name}!")

    user_input = input("Type 'continue' to continue: ").lower()
    addToPrompt(user_input)

    if user_input == "continue":
        print("Loading...")
        legend()














def main():
    generar_menu_aleatorio()
    while True:
        user_input = input()
        addToPrompt(user_input)
        if user_input == "new game":
            new_game_menu()
        elif user_input == "continue":
            # Agrega aquí la lógica para continuar el juego
            pass

        elif user_input == "about":
            about()
            user_input = input()
            addToPrompt(user_input)
            if user_input == "back":
                main()

        elif user_input == "help":
            main_menu_help()
            user_input = input()
            addToPrompt(user_input)
            if user_input == "back":
                main()
            else:
                print("Invalid action, type 'back' to go back to the Main menu")
        if user_input == "exit":
            print("Until the next time")
            break
if __name__ == "__main__":
    main()
