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

def about():
    return """
* About * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             * 
*       Game developed by Team 3, The Link of Zelda :                         *
*                                                                             *
*                                                                             *
*            Ayoub El Bakhti                                                  *
*            Daniel Hirsch                                                    *
*            Denis Fernández                                                  *
*                                                                             *
*                                                                             *
*       Type 'back' now to go back to the 'Main menu'                         *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

def legend():
    return """
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
"""