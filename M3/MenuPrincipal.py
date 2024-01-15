import mysql.connector
from DAzelda import generar_menu_aleatorio
from M3.FuncionesMenu import get_player_name, new_game_menu, help_new_game


cnx = mysql.connector.connect(user='root', password='superlocal', host='127.0.0.1', database='ZeldaSQL')

in_new_game = False 
in_inventory = False
in_saved_games = False
in_main_menu = False


prompt = [""] * 8
player_name = "Link"

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
    for text in prompt:
        print(text)


def process_action(action):
    global prompt
    action = action.lower()

    if action == 'continue':
        add_to_prompt("Continuing the game...")
    elif action == 'new game':
        add_to_prompt("Starting a new game...")
    elif action == 'help':
        add_to_prompt(new_game_menu(player_name))
    elif action == 'about':
        add_to_prompt("About...") 
    elif action == 'exit':
        add_to_prompt("Exiting the game. Goodbye!")
        return True #Indica que el usuario quiere salir del bucle
    else:
        add_to_prompt("Invalid action")

    return False #Indica que el bucle debe continuar



def main():
    clear_prompt()

    while True:
        generar_menu_aleatorio()
        draw_prompt()
        user_input = input("Enter an action: ").lower()
        if process_action(user_input):
            break

main()