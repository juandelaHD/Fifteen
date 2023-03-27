from logica import *

MAXIMOS_MOVIMIENTOS = TOTAL_MOVIMIENTOS*2

def imprimir_interfaz(tablero, cantidad_movimientos):
    """
    Recibe un tablero y lo imprime con formato legible para jugar.
    """
    print("TABLERO:")
    for i in range(CANT_FILAS):
            for j in range(CANT_COLUMNAS):
                    print("|" + str(tablero[i][j]).center(4), end="|")
            print("")
    print(f"""
Controles: w, a, s, d
Salir del juego: o
Movimientos realizados: {cantidad_movimientos} / {MAXIMOS_MOVIMIENTOS}
    """)

def main():

    cantidad_movimientos = 0
    tablero = mezclar_tablero(crear_matriz())  
    
    while cantidad_movimientos < MAXIMOS_MOVIMIENTOS:
        
        imprimir_interfaz(tablero, cantidad_movimientos)

        tablero_ganador = crear_matriz()
        entrada = " "
        entrada = input("Entrada: ")

        mover_ficha(entrada,tablero)
        
        if entrada == "o":
            break

        cantidad_movimientos += len(entrada)
        
        if tablero == tablero_ganador:
            imprimir_interfaz(tablero, cantidad_movimientos)
            print(f"GANASTE! *CARITA FACHERA* ")

    if cantidad_movimientos >= MAXIMOS_MOVIMIENTOS:
        print("Se te acabaron los movimientos. GAME OVER!")

main()