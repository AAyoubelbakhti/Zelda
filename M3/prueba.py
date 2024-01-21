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
generate_item("wooden_shield")
generate_item("shield")
generate_item("sword")
print(inventory)

def toggle_equipment_by_name(name):
    global inventory

    valid_combinations = {
        'wooden_sword': ['wooden_shield', 'shield'],
        'sword': ['wooden_shield', 'shield']
    }

    # Verificar si el nuevo tipo de arma es válido
    weapon_type = next((weapon['type'] for weapon in inventory['weapons'] if weapon['type'] == name), None)
    if weapon_type not in valid_combinations:
        print("Tipo de arma no válido.")
        return inventory

    # Verificar si la combinación es válida con el arma actualmente equipada
    equipped_types = [weapon['type'] for weapon in inventory['weapons'] if weapon['equipped']]
    if equipped_types and not any(combination in valid_combinations.get(equipped_types[0], []) for combination in valid_combinations.get(weapon_type, [])):
        print("Combinación no válida.")
        return inventory

    # Desequipar la nueva arma si ya está equipada
    for weapon in inventory['weapons']:
        if weapon['type'] == weapon_type and weapon['equipped']:
            print(f"{weapon_type} ya está equipada.")
            return inventory

    # Desequipar otras instancias del mismo tipo
    for weapon in inventory['weapons']:
        if weapon['type'] == weapon_type and weapon['equipped']:
            weapon['equipped'] = False
            print(f"{weapon_type} ha sido desequipada.")

    # Equipar la nueva arma
    for weapon in inventory['weapons']:
        if weapon['type'] == weapon_type and not weapon['equipped']:
            weapon['equipped'] = True
            print(f"{weapon_type} ha sido equipada.")
            break
    else:
        print(f"No se encontró {weapon_type} para equipar.")

    return inventory

# Ejemplo de uso:
toggle_equipment_by_name("wooden_sword")
toggle_equipment_by_name("shield")




print(inventory)

toggle_equipment_by_name("wooden_shield")


print(inventory)

toggle_equipment_by_name("sword")

print(inventory)