from zelda.maps import maps
import random
# La idea es hacer algo como Hyrule[3][4] y ir moviendose en un eje X Y.

# Lista de cosas que hacer

# - Santuarios ? a () y curan entero y + 1 max corazon + "Open Sanctuary"
# - Funcio Show map
# - Import Maps
# - Guardar la posicion del user 
# - Canvi seccio, santuari, menjar, get weapon = Save game
# - Las ! son la pos default del personaje
# - Los espacios se pueden atacar con la espada, 1/10 te da lagarto
# - O son piedras
# - C se puede cocinar al lado
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
# Els cofres es tornen a tancar quan estan tots oberts, i el jugador es queda sense cap espasa
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

def movements(ac):
    words = ac.split()
    way = words[1]
    acts = words[2]
    if way == "left":
        #posicion check y intercambiar el " " por "X"
    elif way == "right":
        #
    elif way == "up":
        #
    elif way == "down":
        #
    elif way == "by":
        #Buscar en el mapa la posicion valida mas cercana a lo que pide
    else:
        # go to Hyrule, va al ! de ese mapa, hay 1 mapa inaccesible depende de el mapa en el que estes     

def actions(ac):
    if (ac.split()[0]) == "go":
        movements(ac)
