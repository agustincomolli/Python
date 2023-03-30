from mylib import *


def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    clear_screen()
    print(color_me("*** TA - TE - TI ***\n".center(25), "yellow"))
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        col1, col2, col3 = board[row][0], board[row][1], board[row][2]
        print(f"|   {col1}   |   {col2}   |   {col3}   |")
        print("|       |       |       |")

    print("+-------+-------+-------+\n")


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    pass


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    pass


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    pass


def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    pass


board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]
         ]

display_board(board)