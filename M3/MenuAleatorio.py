import random

def generar_menu_aleatorio():
    opciones = [menu_1, menu_2, menu_3]
    menu_seleccionado = random.choice(opciones)
    return menu_seleccionado()

def menu_1():
    return """   
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

def menu_2():
    return """
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

def menu_3():
    return """
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

