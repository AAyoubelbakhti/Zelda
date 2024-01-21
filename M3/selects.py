from maps import hyrule

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
santuaris = ["S0?", "S1?", "S2?", "S3?", "S4?", "S5?", "S6?"]

def mostrar_mapa():
    for row in hyrule:
        print(' '.join(row))

def es_movimiento_valido(x, y, mapa):
    elementos_invalidos = [roca, arbre, cocina, agua, santuari, fox, enemy, chest, open_chest]

    if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] not in elementos_invalidos and not mapa[x][y].isdigit():
        return True
    return False

def movimientos(ac, mapa, posicion_actual):
    palabras = ac.split()
    
    if len(palabras) != 2 or palabras[0].lower() not in ["up", "down", "left", "right"]:
        print("Comando no reconocido. Usa 'up', 'down', 'left' o 'right' seguido de la cantidad.")
        return posicion_actual

    direccion = palabras[0].lower()
    
    try:
        cantidad = int(palabras[1])
    except ValueError:
        print("La cantidad debe ser un número entero.")
        return posicion_actual

    x, y = posicion_actual

    if direccion == "up" and es_movimiento_valido(x - cantidad, y, mapa):
        mapa[x][y] = gespa
        posicion_actual = (x - cantidad, y)
        mapa[x - cantidad][y] = link
    elif direccion == "down" and es_movimiento_valido(x + cantidad, y, mapa):
        mapa[x][y] = gespa
        posicion_actual = (x + cantidad, y)
        mapa[x + cantidad][y] = link
    elif direccion == "left" and es_movimiento_valido(x, y - cantidad, mapa):
        mapa[x][y] = gespa
        posicion_actual = (x, y - cantidad)
        mapa[x][y - cantidad] = link
    elif direccion == "right" and es_movimiento_valido(x, y + cantidad, mapa):
        mapa[x][y] = gespa
        posicion_actual = (x, y + cantidad)
        mapa[x][y + cantidad] = link
    
    return posicion_actual

def mostrar_inventario(inventario):
    print("\n" + "-" * 56 + "\n")
    print("{:<25}{:>25}".format("Move", "Inventory"))
    print("{:<25}{:>25}".format("----", "---------"))

    for item in inventario:
        print("{:<25}{:>25}".format(item, ""))
    
    print("\n" + "-" * 56 + "\n")

inventario = ["Sword", "Shield", "Key", "Rupees"]

posicion_actual = [7, 11]


