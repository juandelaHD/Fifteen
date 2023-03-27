from random import *

CANT_FILAS = 4
CANT_COLUMNAS = 4

MOVIMIENTO_IZQUIERDA = "a"
MOVIMIENTO_DERECHA = "d"
MOVIMIENTO_ARRIBA = "w"
MOVIMIENTO_ABAJO = "s" 

TOTAL_MOVIMIENTOS = randint(4,30) 

def crear_lista_num():
    '''
    crea una lista con la cantidad máxima de valores posibles según la cantidad de filas y columnas
    '''
    if CANT_FILAS <= 0 or CANT_COLUMNAS <= 0:
        return "La cantidad de filas y columnas debe ser mayor a cero. Por favor, modifique su valor desde el archivo logica.py"
    else:
        lista_num = []
        for i in range(1,CANT_FILAS*CANT_COLUMNAS):
            lista_num.append(i) 
        lista_num.append(0)
        return lista_num

def crear_matriz():
    ''' 
    Crea la matriz a partir de las constantes establecidas.
    '''
    tablero = []
    numeros = crear_lista_num()
    indice = 0
    for _ in range(CANT_FILAS):
        filas = []
        for _ in range(CANT_COLUMNAS):
            filas.append(numeros[indice])
            indice += 1
        tablero.append(filas)
    return tablero

def encontrar_posicion_cero(tablero_movido):
    for i in range(CANT_FILAS):
        for j in range(CANT_COLUMNAS):
            if tablero_movido[i][j] == 0:
                return i, j

def mover_ficha_izquierda(tablero_movido):
    """
    Intercambia la posición del cero y el número que está a su derecha.
    """
    posicion_i, posicion_j = encontrar_posicion_cero(tablero_movido)
    if posicion_j != CANT_COLUMNAS-1:
        tablero_movido[posicion_i][posicion_j+1], tablero_movido[posicion_i][posicion_j] = tablero_movido[posicion_i][posicion_j], tablero_movido[posicion_i][posicion_j+1]

def mover_ficha_derecha(tablero_movido):
    """
    Intercambia la posición del cero y el número que está a su izquierda.
    """
    posicion_i, posicion_j = encontrar_posicion_cero(tablero_movido)
    if posicion_j != 0:
                tablero_movido[posicion_i][posicion_j-1], tablero_movido[posicion_i][posicion_j] = tablero_movido[posicion_i][posicion_j], tablero_movido[posicion_i][posicion_j-1]

def mover_ficha_arriba(tablero_movido):
    """
    Intercambia la posición del cero y el número que está debajo.
    """
    posicion_i, posicion_j = encontrar_posicion_cero(tablero_movido)
    if posicion_i != CANT_FILAS-1:
        tablero_movido[posicion_i+1][posicion_j], tablero_movido[posicion_i][posicion_j] = tablero_movido[posicion_i][posicion_j], tablero_movido[posicion_i+1][posicion_j]

def mover_ficha_abajo(tablero_movido):
    """
    Intercambia la posición del cero y el número que está encima.
    """
    posicion_i, posicion_j = encontrar_posicion_cero(tablero_movido)
    if posicion_i != 0:
        tablero_movido[posicion_i-1][posicion_j], tablero_movido[posicion_i][posicion_j] = tablero_movido[posicion_i][posicion_j], tablero_movido[posicion_i-1][posicion_j]

def mover_ficha(entrada,tablero_movido):
    """
    con el valor ingresado por el usuario, se modificarán las posiciones de los valores de la lista.
    """
    lista_movimientos = []
    for i in entrada.lower():
        lista_movimientos.append(i)

    for i in lista_movimientos:
        if i == MOVIMIENTO_IZQUIERDA:
            mover_ficha_izquierda(tablero_movido)

        elif i == MOVIMIENTO_DERECHA:
            mover_ficha_derecha(tablero_movido)

        elif i == MOVIMIENTO_ARRIBA:
            mover_ficha_arriba(tablero_movido)
                               
        elif i == MOVIMIENTO_ABAJO:
            mover_ficha_abajo(tablero_movido)

        else:
            return tablero_movido   

    return tablero_movido

def mezclar_tablero(tablero):
    """
    Reordena el tablero de cierta forma para que parezca mezclado con determinados movimientos
    """
    mezclas = []
    posibles_mezclas = ["a", "s","d", "w"]        

    for i in range(TOTAL_MOVIMIENTOS):
        mezclas.append(choice(posibles_mezclas))

    for i in mezclas:
        tablero = mover_ficha(i,tablero)

    return tablero