#imports
import os
import platform
import random

#diccionario para el inventario
inventory = {
    ''name': 'link',
    ''BloodMoon': '25',
    'Hearts': {'current': 3, 'max': 3},

    'food': {

    },
    'weapons': {

    }
}


#Función para limpiar la pantalla
def clear_screen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#funciones del prompt
def clearPrompt():
    global prompt
    prompt = [""] * 8

def addToPrompt(text):
    global prompt
    prompt.append(text)
    if len(prompt) > 8:
        prompt.pop(0)

def drawPrompt():
    global prompt
    for text in prompt:
        print(text)

#función para mostrar el inventario
def show_inventory(inventory, category):
    if category == 'help':
        print('* Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
        print("* Type 'show inventory main' to show the main inventory *")
        print("* (main, weapons, Food) *")
        print("* Type 'eat X' to eat X, where X is a Food item *")
        print("* Type 'Cook X' to Cook X, where X is a Food item *")
        print("* Type 'equip X' to equip X, where X is a weapon *")
        print("* Type 'unequip X' to unequip X, where X is a weapon *")
        print("* Type 'back' now to go back to the 'Game' *")
        print("* Back * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    elif category == 'main':
        for key, value in inventory.items():
            print(f'{key}: {value}')
    elif category in inventory:
        print(f'\nInventory {category}: {inventory[category]}')
    else:
        print(f'Category "{category}" not found')

#función para cocinar
def cook(inventory, action):
    if action == 'cook salad':
        if inventory['food']['vegetable'] >= 2:
            inventory['food']['vegetable'] -= 2
            inventory['food']['salad'] += 1
            print('You made cook salad and obtained 1 salad.')
        else:
            print('Not enough vegetables to make salad.')
    elif action == 'cook pescatarian':
        if inventory['food']['fish'] >= 1 and inventory['food']['vegetable'] >= 1:
            inventory['food']['fish'] -= 1
            inventory['food']['vegetable'] -= 1
            inventory['food']['pescatarian'] += 1
            print('You made cook pescatarian and obtained 1 pescatarian.')
        else:
            print('Not enough ingredients to make pescatarian.')
    elif action == 'cook roasted':
        if inventory['food']['meat'] >= 1 and inventory['food']['vegetable'] >= 1:
            inventory['food']['meat'] -= 1
            inventory['food']['vegetable'] -= 1
            inventory['food']['roasted'] += 1
            print('You made cook roasted and obtained 1 roasted.')
        else:
            print('Not enough ingredients to make roasted.')
    else:
        print(f'Unknown action: {action}.')

#función para comer
def eat(inventory, action):
    if action == 'eat vegetable':
        if inventory['food']['vegetable'] >= 1:
            inventory['Hearts']['current'] += 1
            inventory['food']['vegetable'] -= 1
            if inventory['Hearts']['current'] > inventory['Hearts']['max']:
                inventory['Hearts']['current'] = inventory['Hearts']['max']
    elif action == 'eat salad':
        if inventory['food']['salad'] >= 1:
            inventory['food']['salad'] -= 1
            inventory['Hearts']['current'] += 2
            if inventory['Hearts']['current'] > inventory['Hearts']['max']:
                inventory['Hearts']['current'] = inventory['Hearts']['max']
    elif action == 'eat pescatarian':
        if inventory['food']['pescatarian'] >= 1:
            inventory['food']['pescatarian'] -= 1
            inventory['Hearts']['current'] += 3
            if inventory['Hearts']['current'] > inventory['Hearts']['max']:
                inventory['Hearts']['current'] = inventory['Hearts']['max']
    elif action == 'eat roasted':
        if inventory['food']['roasted'] >= 1:
            inventory['food']['roasted'] -= 1
            inventory['Hearts']['current'] += 4
            if inventory['Hearts']['current'] > inventory['Hearts']['max']:
                inventory['Hearts']['current'] = inventory['Hearts']['max']

#función trampas (incompleta)
def cheat(inventory, action):
    elif action == 'cheat rename':

        inventory['name'] = 'Neu Name'
    if action == 'cheat add vegetable':
        inventory['food']['vegetable'] += 1
    elif action == 'cheat add fish':
        inventory['food']['fish'] += 1
    elif action == 'cheat add meat':
        inventory['food']['meat'] += 1
    elif action == 'cheat cook salad':
        cook(inventory, 'cook salad')
    elif action == 'cheat cook pescatarian':
        cook(inventory, 'cook pescatarian')
    elif action == 'cheat cook roasted':
        cook(inventory, 'cook roasted')
    elif action == 'cheat add wood sword':
        inventory['weapons']['wood sword'] = {'attack': 1, 'durability': 5}
    elif action == 'cheat add sword':
        inventory['weapons']['sword'] = {'attack': 1, 'durability': 9}
    elif action == 'cheat add wood shield':
        inventory['weapons']['wood shield'] = {'durability': 5}
    elif action == 'cheat add shield':
        inventory['weapons']['shield'] = {'durability': 9}
    elif action == cheat open sanctuaries:

    elif action == cheat game over:

    elif action == cheat win game:
