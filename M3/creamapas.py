#Atencion: Esta funcion no es necesaria, solo sirve para generar los mapas en forma de lista
def imprimir_texto():
    texto_entrada = """
* Castle  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                         *                   *
*        \ /                              Ganon ♥♥♥♥♥♥♥♥  *                   *
*      -- O --                                            *                   *
*        / \                                              *                   *
*                             |>  v-v-v-v   |>            *                   *
*                     ,   ,  /_\  |     |  /_\            *                   *
*                     |\_/|  | |'''''''''''| |            *                   *
*                     (q p),-| | ||  _  || | |'-._  |\    *                   *
* OT!               X  \_/_(/| |    |#|    | | )  '-//    *                   *
* OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO*                   * 
* Back, Go, Attack  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *



"""
     
    lineas = texto_entrada.strip().split('\n')
    array_resultado = [list(linea) for linea in lineas]

    for fila in array_resultado:
        print('[', end='')
        for i, caracter in enumerate(fila):
            if i > 0:
                print(', ', end='')
            print(f'\'{caracter}\'', end='')
        print(']')

imprimir_texto()
