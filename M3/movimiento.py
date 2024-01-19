from M3.maps import maps, santuaris
import random
from diccionarios import inventory, item_counters
from comida import cook
from inventario import generate_item
from FuncionesPrompt import addToPrompt
# Lista de cosas que hacer

# - Canvi seccio, santuari, menjar, get weapon = Save game
# go to Hyrule, anirà al ! ‘Hyrule’
# Hyrule X Necluda
# Death Mountain X Gerudo

gespa = " "
spawn = "!"
roca = "O"
cocina = "C"
arbre = "T"
#If arbre mapa[x][y+1] isnumber, False
agua = "~"
fox = "F"
santuari = "S"
#If santuari pos +2 is "?", then "?" = " "
link = "X"
chest = "M"
open_chest = "W"
enemy = "E"
pos_link = maps["Hyrule"][6][11]
Hyrule = maps["Hyrule"]
def show_map(): #Esto muestra el mapa, pero tiene que cuadrar dentro de los *.
    for row in maps["global"]:
        print(row)

def atk_gespa(current_position,mapa):
    x,y = current_position
    if mapa(x+1,y) == gespa or mapa(x,y+1) == gespa or mapa(x,y-1) == gespa or mapa(x-1,y) == gespa:
        lagarto = random.randint(1, 100)
        if lagarto <= 10:
            generate_item("meat")
            addToPrompt("You got a Lizard.")
        else:
            addToPrompt("Nothing happened.")

def sanctuary():
# - Santuarios ? a () y curan entero y + 1 max corazon + "Open Sanctuary"

def atk_tree(current_position,mapa):
    x,y = current_position
    if mapa(x+1,y) == arbre or mapa(x,y+1) == arbre or mapa(x,y-1) == arbre or mapa(x-1,y) == arbre and tree_hp != 0:
        if not espada_carregada:
            ob = random.randint(1,100)
            if ob <= 40:
                generate_item("vegetable")
                addToPrompt("You got an apple.")
            elif 40 < ob <= 50:
                ee = random.randint(0,1)
                if ee == 0:
                    generate_item("wooden_sword")
                    addToPrompt("You got a Wood sword.")
                else: 
                    generate_item("wooden_shield")
                    addToPrompt("You got a Wood shield.")
            else:
                addToPrompt("The tree didn't give you anything.")
        else:
            ob = random.randint(1,100)
            if ob <= 40:
                generate_item("vegetable")
                addToPrompt("You got an apple.")
            elif 40 < ob <= 60:
                generate_item("wooden_sword")
                addToPrompt("You got a Wood sword.")
            elif 60 < ob <= 80:
                generate_item("wooden_shield")
                addToPrompt("You got a Wood shield.")
            else:
                addToPrompt("The tree didn't give you anything.")
            sword_hp = sword_hp - 1
            tree_hp = tree_hp - 1
            if tree_hp == 0:
                # Creo que habra que ponerle vidas a cada arbol, para asi meterle su contador

def fish():
# - ~ se obtiene pez 20%. Cuando se obtiene un pez, hasta que no se salga del mapa no respawnea. 

def fox():
# - F solo se ve el 50% de las veces. Y se avisa si hay

def chest():
# - M cofres
# Hyrule i Gerudo espases
# Death Mountain i Necluda escuts
# -W, un cofre obert
    
def enemy():
# Los enemigos tienen vida y cuando mueren desaparecen.
# Cuando atacas te quitan 1 corazon y se mueven 1 posicion



















































def is_valid_move(x, y, mapa):
    if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] != roca and mapa[x][y] != arbre and mapa[x][y] != cocina and mapa[x][y] != agua:
        return True
    return False

def movements(ac, mapa, current_position):
    words = ac.split()
    way = words[1]
    acts = int(words[2])

    x, y = current_position

    if way == "left" and is_valid_move(x, y - acts, mapa):
        mapa[x][y] = gespa
        current_position = (x, y - acts)
        mapa[x][y - acts] = link
    elif way == "right" and is_valid_move(x, y + acts, mapa):
        mapa[x][y] = gespa
        current_position = (x, y + acts)
        mapa[x][y + acts] = link
    elif way == "up" and is_valid_move(x - acts, y, mapa):
        mapa[x][y] = gespa
        current_position = (x - acts, y)
        mapa[x - acts][y] = link
    elif way == "down" and is_valid_move(x + acts, y, mapa):
        mapa[x][y] = gespa
        current_position = (x + acts, y)
        mapa[x + acts][y] = link
    elif way == "by":
        # Implementa la búsqueda de la posición más cercana
    else:
        # Implementa el movimiento especial, por ejemplo, "go to Hyrule"

    return current_position













def actions(ac, mapa, current_position):
    if ac.split()[0] == "go":
        current_position = movements(ac, mapa, current_position)
    elif ac == "show map":
        show_map()
    elif ac == "attack grass" and #Equipped Sword:
        atk_gespa(current_position,mapa)
    elif ac == "attack tree":
        atk_tree(current_position,mapa)
    return current_position
