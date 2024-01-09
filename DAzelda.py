import random 

def generar_figura_aleatoria():
    opciones = [figura_1, figura_2, figura_3]
    figura_seleccionada = random.choice(opciones)
    figura_alineada = alinear_a_derecha(figura_seleccionada())
    return figura_alineada

def alinear_a_derecha(figura):
    return "\n".join(linea.rjust(20) for linea in figura.splitlines())


def figura_1():
    return"""   
    
                               &&
                               &&
                             ##OOO
                            ###OOOO
                            ###OOO \
                              |@@@| \
                              |   |  \
                              =   ==
                           %%%%%%%%%%%%
                         %%%%%%%%%%%%%%%    
        
    """

def figura_2():
    return """

                                &&
                               oo &
                     $         -- &##
                      $$      <<OO####
                       $$  / /OOO####
                        $$/ / OO#####
                         **    OOO###
                          &    @@@@\
                               Q  Q
                               Q  Q

                               

"""

def figura_3():
    return """

                                &&
                               ####
                              " || "
                           @@@@@@@@@@@@
                          @     ||@@@
                                |@@@
                               @@@
                             @@@||     @         
                          @@@@@@@@@@@@@
                                ||
"""

figura_aleatoria = generar_figura_aleatoria()
print(figura_aleatoria)