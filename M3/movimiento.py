from M3.maps import maps, santuaris
import random
# La idea es hacer algo como Hyrule[3][4] y ir moviendose en un eje X Y.

# Lista de cosas que hacer

# - Santuarios ? a () y curan entero y + 1 max corazon + "Open Sanctuary"
# - Funcio Show map
# - Canvi seccio, santuari, menjar, get weapon = Save game
# - Los espacios se pueden atacar con la espada, 1/10 te da lagarto
# - T y TX.
# Puños: 40% poma, 10% espada madera o escudo madera
# Espada: 40% poma, 20% espada madera o escudo madera, Espada -1 uso 
# Arboles: 4 golpes muere durante 10 movimientos, X es el numero de movimientos left
# - ~ se obtiene pez 20%. Cuando se obtiene un pez, hasta que no se salga del mapa no respawnea. 
# - F solo se ve el 50% de las veces. Y se avisa si hay
# - X (LINK) go left X
# Go by X (Nom zona) - Recorrer toda la lista hasta el lugar mas cercano i guess
# go to Hyrule, anirà al ! ‘Hyrule’
# Hyrule X Necluda
# Death Mountain X Gerudo
# - M cofres
# Hyrule i Gerudo espases
# Death Mountain i Necluda escuts
# -W, un cofre obert
# - EX 
# Los enemigos tienen vida y cuando mueren desaparecen.
# Cuando atacas te quitan 1 corazon y se mueven 1 posicion
# - Castillo lo ultimo


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
    return current_position
