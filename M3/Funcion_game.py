# selects.py
from inventario import show_inventory
from diccionarios import inventory
from maps import hyrule

def mostrar_mapa():
    for row in hyrule:
        print(' '.join(row))

def es_movimiento_valido(x, y, mapa):
    elementos_invalidos = ["O", "T", "C", "~", "S", "F", "E", "M", "W"]
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
        mapa[x][y] = " "
        posicion_actual = (x - cantidad, y)
        mapa[x - cantidad][y] = "X"
    elif direccion == "down" and es_movimiento_valido(x + cantidad, y, mapa):
        mapa[x][y] = " "
        posicion_actual = (x + cantidad, y)
        mapa[x + cantidad][y] = "X"
    elif direccion == "left" and es_movimiento_valido(x, y - cantidad, mapa):
        mapa[x][y] = " "
        posicion_actual = (x, y - cantidad)
        mapa[x][y - cantidad] = "X"
    elif direccion == "right" and es_movimiento_valido(x, y + cantidad, mapa):
        mapa[x][y] = " "
        posicion_actual = (x, y + cantidad)
        mapa[x][y + cantidad] = "X"
    
    return posicion_actual

def mostrar_inventario(inventario):
    print("\n" + "-" * 56 + "\n")
    print("{:<25}{:>25}".format("Move", "Inventory"))
    print("{:<25}{:>25}".format("----", "---------"))

    for item in inventario:
        print("{:<25}{:>25}".format(item, ""))
    
    print("\n" + "-" * 56 + "\n")

def game():
    inventario = inventory
    posicion_actual = [7, 11]

    while True:
        mostrar_mapa()
        ac = input("Mover: ")

        if ac.lower() == "continue":
            break
        elif ac.lower().startswith("show inventory"):
            _, category = ac.lower().split(" ", 2)
            show_inventory(inventario, category)
        elif ac.lower() == "show map":
            mostrar_mapa()
        elif ac.lower().startswith("move"):
            _, direction, quantity = ac.lower().split(" ", 3)
            cantidad = int(quantity)
            # Lógica de movimiento aquí, similar a tu código anterior
            posicion_actual = movimientos(ac, hyrule, posicion_actual)
        else:
            print("Comando no reconocido. Intenta de nuevo.")

# Example of how to use it
game()
















