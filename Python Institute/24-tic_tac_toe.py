from mylib import *
from random import randrange


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


def make_list_of_fields(board):
    """
    Description: Crea una lista compuesta de tuplas que tienen un par de 
                 valores que indican las filas y las columnas de cada
                 posición del tablero.
    """

    positions = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            positions.append((row, col))

    return positions


def validate_input(move_input:str):
    """
    Description: Valida que lo que ingresa el usuario sea un número entero
                 entre 1 y 9.
    """
    
    try:
        move = int(move_input)
        if move < 1 or move > 9:
            raise ValueError
        return move
    except ValueError:
        raise ValueError("Debe ingresar un número entre 1 y 9")


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    free_fields = make_list_of_free_fields(board)
    positions = make_list_of_fields(board)
    while True:
        display_board(board)
        move_input = input_color("Ingresa tu movimiento: ", "green")
        try:
            move = validate_input(move_input)
            # Verificar que la posición elegida esté libre.
            if positions[move-1] in free_fields:
                break
            else:
                raise ValueError("Posición ocupada por el oponente.")
        except ValueError as e:
            show_error(str(e))
            press_enter_to_continue()
    
    # Actualizar el tablero ocupando la posición elegida.
    row, col = positions[move-1]
    board[row][col] = color_me("O", "blue")


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_fields = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != "X" and board[row][col] != "O":
                free_fields.append((row, col))
    
    return free_fields


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    pass


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    free_fields = make_list_of_free_fields(board)
    move = randrange(len(free_fields))
    row, col = free_fields[move]
    board[row][col] = "X"


board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

board[1][1] = color_me("X", "red")
enter_move(board)
display_board(board)