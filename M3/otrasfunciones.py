import os
import platform
from diccionarios import inventory, item_counters


#Función para limpiar la pantalla
def clear_screen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#función para  el contador de blood moon (falta la parte para regenerar los  bichos)
def decrease_blood_moon(inventory):
    blood_moon = int(inventory['BloodMoon'])
    if blood_moon > 0:
        blood_moon -= 1
        inventory['BloodMoon'] = str(blood_moon)
    else:
        inventory['BloodMoon'] = '25'


