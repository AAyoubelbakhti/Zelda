import random

def generar_menu_aleatorio():
    opciones = [menu_1, menu_2, menu_3]
    menu_seleccionado = random.choice(opciones)
    return menu_seleccionado()

def menu_1():
    messages = []
    menu_1_text = """   
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *    
*                                                                &&           *
*                                                                &&           *
*                                                             ##OOO           *
*                                                            ###OOOO          *
*                                                            ###OOO \         *
*  Zelda, Breath of the Wild                                   |@@@| \        *
*                                                              |   |  \       *
*                                                              =   ==         *
*                                                           %%%%%%%%%%%%      *
*                                                        %%%%%%%%%%%%%%%      *   
*                                                                             *                                                                            
* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *       
"""

    messages.append(menu_1_text)
    return messages


def menu_2():
    messages = []
    menu_2_text = """
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*                                                                &&           *
*                                                               oo &          *
*                                                       $       -- &##        *
*                                                       $$     <<OO####       *
*                                                        $$  //OOO####        *
*  Zelda, Breath of the Wild                              $$// OO#####        * 
*                                                         **    OOO###        *
*                                                          &    @@@@\         *
*                                                               Q  Q          *
*                                                               Q  Q          *
*                                                                             *
* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * 
"""

    messages.append(menu_2_text)
    return messages


def menu_3():
    messages = [] 
    menu_3_text = """
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                &&           *
*                                                               ####          *
*                                                               "|| "         *
*                                                           @@@@@@@@@@@@      *
*                                                           @    ||@@@        *
*  Zelda, Breath of the Wild                                     |@@@         *
*                                                               @@@           *
*                                                             @@@||     @     *    
*                                                           @@@@@@@@@@@@@     *
*                                                                ||           *
*                                                                             *
* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *   
"""
    messages.append(menu_3_text)
    return messages
