def crear_tablero():
    """Crear un diccionario con las coordenadas de un 
    tablero de ajedrez y crear un diccionario con las piezas del juego."""

    # Crear un diccionario con las coordenadas del tablero.
    tablero = {}
    for fila in range(1,9):
        for columna in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            tablero[f"{fila}{columna}"] = ""
    
    # Crear un diccionario con todas las piezas del ajedrez.
    piezas = {
    "b_rey": 1,
    "b_reina": 1,
    "b_alfil": 2,
    "b_caballo": 2,
    "b_torre": 2,
    "b_peon": 8,
    "n_rey": 1,
    "n_reina": 1,
    "n_alfil": 2,
    "n_caballo": 2,
    "n_torre": 2,
    "n_peon": 8,
    }
    
    return tablero, piezas


def es_cantidad_valida(cantidad_piezas, piezas_ajedrez):
    """Cuenta la cantidad de piezas que hay en el tablero. Si está dentro
    de las cantidades máximas devuelve True."""
    cantidad_piezas = dict(cantidad_piezas)
    piezas_ajedrez = dict(piezas_ajedrez)
    mensaje = ""
    for pieza, cantidad in cantidad_piezas.items():
        if cantidad > piezas_ajedrez[pieza]:
            mensaje = f"Exceso en número de pieza ('{pieza}' = '{cantidad}'),"
            mensaje += f" la canidad máxima es {piezas_ajedrez[pieza]}."
            # print(mensaje)
            return False, mensaje
    return True, mensaje


def es_tablero_valido(tablero_ajedrez):
    """Devuelve True si el tablero a probar es correcto."""
    tablero_ajedrez = dict(tablero_ajedrez)
    tablero, piezas = crear_tablero()
    recuento = {}
    mensaje= ""

    # Chequear que las coordenas y las piezas sean válidas.
    for coordenada, pieza in tablero_ajedrez.items():
        if coordenada not in tablero:
            # print(f"La coordenada {coordenada} es inexistente.")
            mensaje = f"La coordenada '{coordenada}' no existe en un "
            mensaje += "tablero de ajedrez."
            return False, mensaje
        elif pieza not in piezas:
            # print(f"La pieza {pieza} no es una pieza de ajedrez.")
            mensaje = f"La pieza '{pieza}' no es una pieza de ajedrez."
            return False, mensaje
        
        # Contar la cantidad de piezas en el tablero a probar.
        recuento.setdefault(pieza, 0)
        recuento[pieza] += 1

    cantidad_valida, mensaje = es_cantidad_valida(recuento, piezas)
    if cantidad_valida:
        return True, mensaje
    else: 
        return False, mensaje


def mostrar_resultado(prueba):
    """Muestra el resultado de la prueba si es un tablero válido."""
    resultado = es_tablero_valido(prueba)
    if resultado[0]:
        print("Es un tablero válido.")
    else:
        print(resultado[1])


prueba = {'1h': 'n_rey', '6c': 'b_reina', '2g': 'n_alfil', '5h': 'n_reina', 
    '3e': 'b_rey', '1a': 'n_alfil', '2a': 'n_alfil'}
mostrar_resultado(prueba)

prueba = {"8a": "n_peon","8b": "n_peon","8c": "n_peon","8d": "n_peon",
    "8e": "n_peon","8f": "n_peon","8g": "n_peon","8h": "n_peon",}
mostrar_resultado(prueba)

prueba = {'1a': 'n_rey', '6c': 'w_reina', '2g': 'n_alfil', '5h': 'n_reina'}
mostrar_resultado(prueba)

prueba = {'1a': 'n_rey', '6c': 'b_reina', '10g': 'n_alfil', '5h': 'n_reina'}
mostrar_resultado(prueba)
