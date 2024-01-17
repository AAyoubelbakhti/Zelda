#imports
import os
import platform
import random

#diccionario para el inventario
inventory = {
    'name': 'link',
    'BloodMoon': '25',
    'Hearts': {'current': 3, 'max': 3},
    'food': {},
    'weapons': []
}

# diccionario de contadores
item_counters = {
    'wooden_sword': 0,
    'wooden_shield': 0,
    'sword': 0,
    'shield': 0,
    'vegetable': 0,
    'fish': 0,
    'meat': 0,
    'salad': 0,
    'pescatarian': 0,
    'roasted': 0
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


#función para  el contador de blood moon (faltala parte para regenerar los  bichos)
def decrease_blood_moon(inventory):
    blood_moon = int(inventory['BloodMoon'])
    if blood_moon > 0:
        blood_moon -= 1
        inventory['BloodMoon'] = str(blood_moon)
    else:
        inventory['BloodMoon'] = '25'

# función para generar el item y añadirlo al contador
def generate_item(item_type):
    if item_type in item_counters:
        item_counters[item_type] += 1
        item_id = item_counters[item_type]
        durability_max = 5 if 'wooden' in item_type else 9
        if item_type.startswith(('wooden_sword', 'wooden_shield', 'sword', 'shield')):
            inventory['weapons'].append({"id": item_id, "type": item_type, "durability": {"current": durability_max, "max": durability_max}})
        else:
            inventory['food'].setdefault(item_type, 0)
            inventory['food'][item_type] += 1
            return {"id": item_id, "type": item_type}
    else:
        raise ValueError("Invalid item type. Supported types: 'wooden_sword', 'wooden_shield', 'sword', 'shield', 'vegetable', 'fish', 'meat', 'salad', 'pescatarian', 'roasted'")


#función trampas (incompleta)
def cheat(inventory, action):
    elif action == 'cheat rename':
        inventory['name'] = 'Neu Name'
    if action == 'cheat add vegetable':
        generate_item("vegetable")
    elif action == 'cheat add fish':
        generate_item("fish")
    elif action == 'cheat add meat':
        generate_item("meat")
    elif action == 'cheat cook salad':
        cook(inventory, 'cook salad')
    elif action == 'cheat cook pescatarian':
        cook(inventory, 'cook pescatarian')
    elif action == 'cheat cook roasted':
        cook(inventory, 'cook roasted')
    elif action == 'cheat add wood sword':
        generate_item("wooden_sword")
    elif action == 'cheat add sword':
        generate_item("sword")
    elif action == 'cheat add wood shield':
        generate_item("wooden_shield")
    elif action == 'cheat add shield':
        generate_item("shield")
    elif action == cheat open sanctuaries:

    elif action == cheat game over:

    elif action == cheat win game:

