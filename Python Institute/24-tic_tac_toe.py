from mylib import *
from random import randrange


def display_board(board: list):
    """
    Description: Mostrar el tablero en la consola según el estado de board.
    Parameters:  - board: lista que contiene el tablero de TA-TE-TI
    """
    clear_screen()
    print(color_me("*** TA - TE - TI ***\n".center(25), "yellow"))
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        col1, col2, col3 = board[row][0], board[row][1], board[row][2]
        print(f"|   {col1}   |   {col2}   |   {col3}   |")
        print("|       |       |       |")

    print("+-------+-------+-------+\n")


def get_positions(board: list):
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


def get_free_positions(board: list):
    """
    Description: Devuelve una lista con todos los cuadros vacíos del tablero.
    Return:      La lista esta compuesta por tuplas, cada tupla es un par de 
                 números que indican la fila y columna.
    """

    player_sign = color_me("O", "blue")
    machine_sign = color_me("X", "red")

    free_fields = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != machine_sign and board[row][col] != player_sign:
                free_fields.append((row, col))

    return free_fields


def validate_move(move_input: str):
    """
    Description: Valida que lo que ingresa el usuario sea un número entero
                 entre 1 y 9.
    """

    try:
        move = int(move_input)
        if move < 1 or move > 9:
            raise ValueError("Debe ingresar un número entre 1 y 9.")
        return move
    except ValueError as error:
        if str(error) == "Debe ingresar un número entre 1 y 9.":
            raise ValueError(str(error))
        else:
            raise ValueError("Debe ingresar un número entero")


def enter_move(board: list):
    """
    Description: Preguntar al usuario acerca de su movimiento, verificar la 
                 entrada y actualizar el tablero acorde a la decisión del 
                 usuario.
    """
    free_fields = get_free_positions(board)
    positions = get_positions(board)
    while True:
        move_input = input_color("Ingresa tu movimiento: ", "green")
        try:
            move = validate_move(move_input)
            # Verificar que la posición elegida esté libre.
            if positions[move-1] in free_fields:
                break
            else:
                raise ValueError("¡Ops! Posición ocupada 🤔")
        except ValueError as e:
            show_error(str(e))
            press_enter_to_continue()
        display_board(board)


    # Actualizar el tablero ocupando la posición elegida.
    row, col = positions[move-1]
    board[row][col] = color_me("O", "blue")


def victory_for(board: list, sign: str):
    """
    Description: Verifica si, en una línea horizontal o vertical o en las 
                 diagonales del tablero, hay tres signos iguales con lo que
                 se verificaría una victoria.
    Parameters:  - board: tablero.
                 - sign:  es el signo a verificar, si es "O" es el jugador y si
                          es "X" es la máquina.
    """

    is_winner = False
    # Recorrer las filas del tablero.
    for row in range(len(board)):
        if board[row][0] == sign and board[row][1] == sign and \
                board[row][2] == sign:
            is_winner = True
            break
    if not is_winner:
        # Recorrer las columnas del tablero.
        for col in range(len(board)):
            if board[0][col] == sign and board[1][col] == sign and \
                    board[2][col] == sign:
                is_winner = True
                break
    # Chequear las diagonales.
    if not is_winner:
        is_winner = board[0][0] == sign and board[1][1] == sign and \
            board[2][2] == sign
    if not is_winner:
        is_winner = board[2][0] == sign and board[1][1] == sign and \
            board[0][2] == sign

    return is_winner


def draw_move(board: list):
    """
    Description: Generar la selección de la máquina y actualizar el tablero.
    """

    free_fields = get_free_positions(board)
    move = randrange(len(free_fields))
    row, col = free_fields[move]
    board[row][col] = color_me("X", "red")


board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

player_sign = color_me("O", "blue")
machine_sign = color_me("X", "red")

board[1][1] = machine_sign

while True:
    # Dibujar el tablero.
    display_board(board)

    # Chequear si hay una victoria del jugador, del oponente o si hay empate.
    # En caso que ocurra una de estas tres opciones salir del juego.
    if victory_for(board, player_sign):
        print(color_me("\n¡Enhorabuena, has ganado la partida! 🥳\n", "magenta"))
        press_enter_to_continue()
        break
    elif victory_for(board, machine_sign):
        print(color_me("Oh no, has perdido. Mejor suerte para la próxima. 😭", "magenta"))
        press_enter_to_continue()
        break
    elif len(get_free_positions(board)) == 0:
        print(color_me("¡Empate! Intentalo de nuevo.🤝", "magenta"))
        press_enter_to_continue()
        break
    
    # El jugador ingresa su movimiento.
    enter_move(board)
    # La máquina hace su movimiento.
    draw_move(board)
