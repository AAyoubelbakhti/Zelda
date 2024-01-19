from diccionarios import inventory, item_counters


def generate_item(item_type):
    if item_type in item_counters:
        item_counters[item_type] += 1
        item_id = item_counters[item_type]
        durability_max = 5 if 'wooden' in item_type else 9
        if item_type.startswith(('wooden_sword', 'wooden_shield', 'sword', 'shield')):
            inventory['weapons'].append({"id": item_id, "type": item_type, "durability": {"current": durability_max, "max": durability_max}, "equipped": False })
        else:
            inventory['food'].setdefault(item_type, 0)
            inventory['food'][item_type] += 1
            return {"id": item_id, "type": item_type}
    else:
        raise ValueError("Invalid item type. Supported types: 'wooden_sword', 'wooden_shield', 'sword', 'shield', 'vegetable', 'fish', 'meat', 'salad', 'pescatarian', 'roasted'")
    


generate_item("wooden_sword")
generate_item("wooden_sword")
generate_item("wooden_sword")
generate_item("wooden_sword")
generate_item("wooden_sword")
generate_item("wooden_sword")
print(inventory)



def equip_weapon_by_name(name):
    global inventory
    for weapon in inventory['weapons']:
        if weapon['type'] == name and weapon['equipped'] is False:
            weapon['equipped'] = True
            return inventory
    else:
        print("No tienes ese arma o ya está equipada.")
        return inventory

equip_weapon_by_name("wooden_sword")
print(inventory)

def unequip_weapon_by_name(name):
    global inventory
    for weapon in inventory['weapons']:
        if weapon['type'] == name and weapon['equipped']:
            weapon['equipped'] = False
            print(f"{name} ha sido desequipada.")
            return inventory
    else:
        print("No tienes ese arma o no está equipada.")
        return inventory
    
unequip_weapon_by_name("wooden_sword")

print(inventory)