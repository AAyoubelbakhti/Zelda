import mysql.connector
from MenuAleatorio import generar_menu_aleatorio
from FuncionesHelp import help_new_game, inventory_help, saved_games_help, main_menu_help, about
from NewGame import new_game_menu, legend, plot
from FuncionesPrompt import addToPrompt,clearPrompt,drawPrompt
from otrasfunciones import clear_screen




cnx = mysql.connector.connect(user='root', password='superlocal', host='127.0.0.1', database='ZeldaSQL')



prompt = [""] * 8
player_name = "Link"




def main():
    generar_menu_aleatorio()
    while True :
        user_input = input()
        if user_input == "new game":
            addToPrompt(user_input)
            new_game_menu()        




