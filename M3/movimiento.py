from maps import map,hyrule , gerudo ,necluda,castle
import random
from diccionarios import inventory, item_counters
from comida import cook
from inventario import generate_item
from FuncionesPrompt import addToPrompt

# - Canvi seccio, santuari, menjar, get weapon = Save game
# go to Hyrule, anirà al ! ‘Hyrule’
# Hyrule X Necluda
# Death Mountain X Gerudo





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

def show_map(mapa):
    for row in mapa:
        print(' '.join(row))

def attack(ac,current_position,mapa):
    words = ac.split()
    blanc = words[1]
    x,y = current_position
    if blanc == "grass":
        if mapa(x+1,y) == gespa or mapa(x,y+1) == gespa or mapa(x,y-1) == gespa or mapa(x-1,y) == gespa:
            lagarto = random.randint(1, 100)
            if lagarto <= 10:
                generate_item("meat")
                addToPrompt("You got a Lizard.")
            else:
               addToPrompt("Nothing happened.")
    elif blanc == "tree":
            if mapa(x+1,y) == arbre or mapa(x,y+1) == arbre or mapa(x,y-1) == arbre or mapa(x-1,y) == arbre and tree_hp != 0:
                if not inventory["weapons"]["charged"]:
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
                        False




def fish(current_position, mapa):
    x,y = current_position
    if mapa(x+1,y) == agua or mapa(x,y+1) == agua or mapa(x,y-1) == agua or mapa(x-1,y) == agua:
        peix = random.randint(1,100)
        if peix <= 20:
            generate_item("fish")
            addToPrompt("You got a fish.")
            fish_alive = False
        else:
            addToPrompt("You didn't get a fish.")


def open(ac,current_position,mapa):
    words = ac.split()
    blanc = words[1]
    x,y = current_position

 

        













def isvalid(x, y, mapa):
    elementos_invalidos = [roca, arbre, cocina, agua, santuari, fox, enemy, chest, open_chest]

    if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] not in elementos_invalidos and not mapa[x][y].isdigit():
        return True
    return False

def movements(ac, mapa, posicion_actual):
    palabras = ac.split()
    direccion = palabras[1]
    cantidad = int(palabras[2])

    x, y = posicion_actual

    if direccion == "left" and isvalid(x, y - cantidad, mapa):
        mapa[x][y] = gespa
        posicion_actual = (x, y - cantidad)
        mapa[x][y - cantidad] = link
    elif direccion == "right" and isvalid(x, y + cantidad, mapa):
        mapa[x][y] = gespa
        posicion_actual = (x, y + cantidad)
        mapa[x][y + cantidad] = link
    elif direccion == "up" and isvalid(x - cantidad, y, mapa):
        mapa[x][y] = gespa
        posicion_actual = (x - cantidad, y)
        mapa[x - cantidad][y] = link
    elif direccion == "down" and isvalid(x + cantidad, y, mapa):
        mapa[x][y] = gespa
        posicion_actual = (x + cantidad, y)
        mapa[x + cantidad][y] = link
    
    return posicion_actual







def actions(ac, mapa, current_position):
    words = ac.split()
    action = words[0]
    if action == "go":
        current_position = movements(ac, mapa, current_position)
    elif ac == "show map":
        show_map()
    elif action == "attack":
        attack(ac,current_position,mapa)
    elif action == "fish":
        fish(current_position,mapa)
    elif action == "open":
        open(ac,current_position,mapa)
        
    return current_position








class Nearby:
    global currentMap
    def init(self, x, y):
        self.top_left = currentMap[x-1][y-1]
        self.top = currentMap[x, y-1]
        self.top_right = currentMap[x+1, y-1]

        self.left = currentMap[x-1, y]
        self.right = currentMap[x+1, y]

        self.bottom_left = currentMap[x-1, y+1]
        self.bottom = currentMap[x, y+1]
        self.bottom_right = currentMap[x+1, y+1]

nearby = Nearby(7,13)

def moveUp():
    global currentLocaltion, nearby
    if (nearby.top == ' ' ) :
        currentLocaltion = [currentLocaltion[0], currentLocaltion[1]+1]
        nearby = Nearby(currentLocaltion[0], currentLocaltion[1])
    else :
        addToPrompt("You can't move")
        

def moveDown():
    global currentLocaltion, nearby
    if (nearby.bottom == ' ' ) :
        currentLocaltion = [currentLocaltion[0], currentLocaltion[1]-1]
        nearby = Nearby(currentLocaltion[0], currentLocaltion[1])
    else :
        addToPrompt("You can't move")


def moveLeft():
    global currentLocaltion, nearby
    if (nearby.left == ' ' ) :
        currentLocaltion = [currentLocaltion[0]-1, currentLocaltion[1]]
        nearby = Nearby(currentLocaltion[0], currentLocaltion[1])
    else :
        addToPrompt("You can't move")


def moveRight():
    global currentLocaltion, nearby
    if (nearby.right == ' ' ) :
        currentLocaltion = [currentLocaltion[0]+1, currentLocaltion[1]]
        nearby = Nearby(currentLocaltion[0], currentLocaltion[1])
    else :
        addToPrompt("You can't move")