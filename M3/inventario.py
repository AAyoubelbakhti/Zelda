from diccionarios import inventory, item_counters
from comida import cook

#función para mostrar el inventario
def show_inventory(inventory, category):
    if category == 'help':
        print('* Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ')
        print("* Type 'show inventory main' to show the main inventory                    *")
        print("* (main, weapons, Food)                                                    *")
        print("* Type 'eat X' to eat X, where X is a Food item                            *")
        print("* Type 'Cook X' to Cook X, where X is a Food item                          *")
        print("* Type 'equip X' to equip X, where X is a weapon                           *")
        print("* Type 'unequip X' to unequip X, where X is a weapon                       *")
        print("* Type 'back' now to go back to the 'Game'                                 *")
        print("* Back * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    elif category == 'main':
        print(f"* Hearts: {inventory['Hearts']['current']}/{inventory['Hearts']['max']} *")
        for key, value in inventory.items():
            if key == 'weapons':
                print(f'{key}: {", ".join(item for item in value)}')
            elif key == 'food':
                print(f'{key}: {", ".join(f"{food} ({quantity})" for food, quantity in value.items())}')
            else:
                print(f'{key}: {value}')
    elif category in inventory:
        if category == 'weapons':
            print(f'\nInventory {category}: {", ".join(item for item in inventory[category])}')
        elif category == 'food':
            print(f'\nInventory {category}: {", ".join(f"{food} ({quantity})" for food, quantity in inventory[category].items())}')
        else:
            print(f'\nInventory {category}: {inventory[category]}')
    else:
        print(f'Category "{category}" not found')

# función para generar el item y añadirlo al contador
def generate_item(item_type):
    if item_type in item_counters:
        item_counters[item_type] += 1
        item_id = item_counters[item_type]
        durability_max = 5 if 'wooden' in item_type else 9
        if item_type.startswith(('wooden_sword', 'wooden_shield', 'sword', 'shield')):
            inventory['weapons'].append({"id": item_id, "type": item_type, "durability": {"current": durability_max, "max": durability_max}, "equiped": False })
        else:
            inventory['food'].setdefault(item_type, 0)
            inventory['food'][item_type] += 1
            return {"id": item_id, "type": item_type}
    else:
        raise ValueError("Invalid item type. Supported types: 'wooden_sword', 'wooden_shield', 'sword', 'shield', 'vegetable', 'fish', 'meat', 'salad', 'pescatarian', 'roasted'")


#función trampas (incompleta)
def cheat(inventory, action):
    if action == 'cheat rename':
        newName = input("What is your name: ")
        inventory['name'] = newName
    elif action == 'cheat add vegetable':
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
    #elif action == cheat open sanctuaries:

    #elif action == cheat game over:

    #elif action == cheat win game:

