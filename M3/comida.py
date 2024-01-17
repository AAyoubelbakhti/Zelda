from diccionarios import inventory

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


