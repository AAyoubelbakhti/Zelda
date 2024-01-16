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


#función para  el contador de blood moon (faltala parte para regenerar los  bichos)
def decrease_blood_moon(inventory):
    blood_moon = int(inventory['BloodMoon'])
    if blood_moon > 0:
        blood_moon -= 1
        inventory['BloodMoon'] = str(blood_moon)
    else:
        inventory['BloodMoon'] = '25'

#contador de items
wooden_sword_counter = 0
wooden_shield_counter = 0
sword_counter = 0
shield_counter = 0
vegetable_counter = 0
fish_counter = 0
meat_counter = 0
salad_counter = 0
pescatarian_counter = 0
roasted_counter = 0

# función para generar el item y añadirlo al contador
def generate_item(item_type):
    global wooden_sword_counter, wooden_shield_counter, sword_counter, shield_counter
    global vegetable_counter, fish_counter, meat_counter, salad_counter, pescatarian_counter, roasted_counter

    if item_type == "wooden_sword":
        wooden_sword_id = wooden_sword_counter
        wooden_sword_counter += 1
        return {"id": wooden_sword_id, "type": "wooden sword"}
    elif item_type == "wooden_shield":
        wooden_shield_id = wooden_shield_counter
        wooden_shield_counter += 1
        return {"id": wooden_shield_id, "type": "wooden shield"}
    elif item_type == "sword":
        sword_id = sword_counter
        sword_counter += 1
        return {"id": sword_id, "type": "sword"}
    elif item_type == "shield":
        shield_id = iron_shield_counter
        shield_counter += 1
        return {"id": shield_id, "type": "shield"}
    elif item_type == "vegetable":
        vegetable_id = vegetable_counter
        vegetable_counter += 1
        inventory['food']['vegetable'] += 1
        return {"id": vegetable_id, "type": "vegetable"}
    elif item_type == "fish":
        fish_id = fish_counter
        fish_counter += 1
        inventory['food']['fish'] += 1
        return {"id": fish_id, "type": "fish"}
    elif item_type == "meat":
        meat_id = meat_counter
        meat_counter += 1
        inventory['food']['meat'] += 1
        return {"id": meat_id, "type": "meat"}
    elif item_type == "salad":
        salad_id = salad_counter
        salad_counter += 1
        inventory['food']['salad'] += 1
        return {"id": salad_id, "type": "salad"}
    elif item_type == "pescatarian":
        pescatarian_id = pescatarian_counter
        pescatarian_counter += 1
        inventory['food']['pescatarian'] += 1
        return {"id": pescatarian_id, "type": "pescatarian"}
    elif item_type == "roasted":
        roasted_id = roasted_counter
        roasted_counter += 1
        inventory['food']['roasted'] += 1
        return {"id": roasted_id, "type": "roasted"}
    else:
        raise ValueError("Invalid item type. Supported types: 'wooden_sword', 'wooden_shield', 'iron_sword', 'iron_shield', 'vegetable', 'fish', 'meat', 'salad', 'pescatarian', 'roasted'")
