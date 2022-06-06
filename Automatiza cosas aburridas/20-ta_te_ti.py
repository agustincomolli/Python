tablero = {
    "arriba-izq" : " ", "arriba-medio" : " ", "arriba-der" : " ",
    "medio-izq" : " ", "medio-medio" : " ", "medio-der" : " ",
    "abajo-izq" : " ", "abajo-medio" : " ", "abajo-der" : " "
    }

def imprimir_tablero(tablero):
    """Imprime el tablero del Ta-Te-Ti"""
    
    fila1 = str(tablero["arriba-izq"] + "|" + tablero["arriba-medio"] + \
        "|" + tablero["arriba-der"])
    fila2 = str(tablero["medio-izq"] + "|" + tablero["medio-medio"] + \
        "|" + tablero["medio-der"])
    fila3 = str(tablero["abajo-izq"] + "|" + tablero["abajo-medio"] + \
        "|" + tablero["abajo-der"])

    print("\n" + fila1.center(20))
    print("-+-+-".center(20))
    print(fila2.center(20))
    print("-+-+-".center(20))
    print(fila3.center(20))


turno = "X"
for i in range(6):
    print(f"\n*** TA - TE - TI ***\n{'=' *20}\n")
    mueve = input(f"Turno para {turno}. ¿Dónde desea colocar su ficha? ")
    tablero[mueve] = turno
    
    if turno == "X":
        turno = "O"
    else:
        turno = "X"

    imprimir_tablero(tablero)