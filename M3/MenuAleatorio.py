import random
from FuncionesPrompt import drawPrompt

def generar_menu_aleatorio():
    opciones = [menu_1, menu_2, menu_3]
    menu_seleccionado = random.choice(opciones)
    return menu_seleccionado()

def menu_1():
    print("""   
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
""")
    drawPrompt()


def menu_2():
    print("""
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
""")
    drawPrompt()

def menu_3():
    print("""
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
""")
    drawPrompt()