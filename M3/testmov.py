from maps import maps


gespa = " "
spawn = "!"
roca = "O"
cocina = "C"
arbre = "T"
agua = "~"
fox = "F"
santuari = "S"
link = "X"
chest = "M"
open_chest = "W"
enemy = "E"
Hyrule = maps["Hyrule"]

def show_map(): #Esto muestra el mapa, pero tiene que cuadrar dentro de los *.
    for row in maps["Hyrule"]:
        print(' '.join(row))

def is_valid_move(x, y, mapa):
    elementos_invalidos = [roca, arbre, cocina, agua, santuari, fox, enemy, chest, open_chest]

    if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] not in elementos_invalidos and not mapa[x][y].isdigit():
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
    
    return current_position

current_position = [11, 7]
while True:
    show_map()
    ac = input("Move: ")
    movements(ac,Hyrule,current_position)