from comida import cook, eat
from diccionarios import inventory, item_counters
from FuncionesHelp import inventory_help
from FuncionesPrompt import drawPrompt
from maps import maps

from otrasfunciones import clear_screen, decrease_blood_moon
from inventario import generate_item , show_inventory


def print_screen(char_pos, options, mat, map_name, inventory, inv_title="Main", titol_seccio="*"):
    clear_screen()

    # Obtén el mapa correspondiente al nombre proporcionado
    current_map = maps["Hyrule"]

    # Imprime el mapa a la izquierda
    for i in range(len(current_map)):
        print("*", end="")
        for j in range(len(current_map[i])):
            print(current_map[i][j], end="")
        print("*", end="")

        # Imprime la información del inventario a la derecha
        if i < len(inventory):
            if i == 2:  # Imprime las Hearts con el formato adecuado
                print(f" Hearts: {inventory['Hearts']['current']}/{inventory['Hearts']['max']} {' ' * (53 - len(str(inventory['Hearts']['current']) + '/' + str(inventory['Hearts']['max'])))} *")
            else:
                print(f" {' ' * (60 - len(inventory[i]))} {inventory[i]} *")
        else:
            print(" " * 60)

    print("*" * 90)
    print(f"{'*' * (44 - len(options) // 2)} {', '.join(options)} {'*' * (45 - len(options) // 2)}")

    # Agrega la visualización del inventario utilizando la función show_inventory
    show_inventory(inventory['main'], "main")  # Puedes cambiar "main" a la categoría deseada

    drawPrompt()

# Ejemplo de uso:
char_position = [1, 1]
options_list = ["Option 1", "Option 2", "Option 3"]
matrix =  [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', 'O'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'O', 'O', '~', 'O', 'O', 'O', 'O', '~'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~'],
        [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~', ' ', ' ', ' ', '~', '~', '~', '~', '~', '~'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', '9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '~', '~'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '!', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'O', 'O', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', '1', '?', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', 'M', ' ', ' ', ' ', 'F', ' ', ' ', ' ', ' ', ' '],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]

inventory = {
    'name': 'link',
    'BloodMoon': '25',
    'Hearts': {'current': 3, 'max': 3},
    'food': {'Apple': 5},
    'weapons': ['Wood Sword', 'Shield']
}

print_screen(char_position, options_list, matrix, "Hyrule", inventory, inv_title="Inventory", titol_seccio="*")











