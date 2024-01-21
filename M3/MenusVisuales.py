from FuncionesPrompt import drawPrompt, addToPrompt, prompt
from diccionarios import inventory
from Funcion_game import game



def legend():
    print("""
* Legend  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*    10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah  *
*    tribe. The Sheikah were a tribe of warriors who protected the Triforce,  *
*    a sacred relic that granted wishes.                                      *
*                                                                             *
*    But one day, Ganondorf, an evil sorcerer, stole the Triforce and began   *
*    to rule Hyrule with an iron fist.                                        *
*                                                                             *
*    The princess, with the help of a heroic young man, managed to defeat     *
*    Ganondorf and recover the Triforce.                                      *
*                                                                             *
* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
""")
    drawPrompt()
    user_input = input("Type 'continue' to continue: ")
    addToPrompt(user_input)
    if user_input.lower() == "continue":
        plot()
    else:
        print("Invalid action. Please type 'continue' to continue")



def plot():
    print(f"""
* Plot  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*  Now history is repeating itself, and Princess Zelda has been captured by   *
*  Ganon. He has taken over the Guardians and filled Hyrule with monsters.    *
*                                                                             *
*                                                                             *
*  But a young man named '{inventory["name"]}' has just awakened and                        *
*  must reclaim the Guardians to defeat Ganon and save Hyrule.                *
*                                                                             *
*                                                                             *
* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")
    drawPrompt()
    user_input = input("Type 'continue' to continue: ")
    addToPrompt(user_input)
    if user_input.lower() == "continue":
        game()
    else:
        print("Invalid action. Please type 'continue' to continue")
