from comida import cook, eat
from diccionarios import inventory, item_counters
from FuncionesHelp import inventory_help
from FuncionesPrompt import *
from inventario import show_inventory, generate_item
from creamapas import imprimir_texto
from maps import maps, santuaris
from otrasfunciones import clear_screen, decrease_blood_moon


import curses

def game(stdscr):
    # Configuración básica
    curses.curs_set(0)  # Oculta el cursor
    stdscr.clear()

    # Dibuja el mapa
    for i in range(0, curses.COLS):
        stdscr.addch(0, i, '*')
        stdscr.addch(curses.LINES - 1, i, '*')

    for i in range(0, curses.LINES):
        stdscr.addch(i, 0, '*')
        stdscr.addch(i, curses.COLS - 1, '*')

    # Dibuja el inventario
    inventory = [
        "Link        ♥ 3/5",
        "Blood moon in  25",
        "",
        "Equipment",
        "    Wood Sword",
        "    Shield",
        "",
        "Food            5",
        "Weapons        10",
    ]

    for i, item in enumerate(inventory):
        stdscr.addstr(i + 1, curses.COLS // 2 + 1, item)

    stdscr.refresh()
    stdscr.getch()

curses.wrapper(game)
