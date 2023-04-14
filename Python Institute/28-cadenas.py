"""
Escribir tu propia función, que se comporte casi como el método original 
split(), por ejemplo:

Debe aceptar únicamente un argumento: una cadena.
Debe devolver una lista de palabras creadas a partir de la cadena, dividida 
en los lugares donde la cadena contiene espacios en blanco.
Si la cadena está vacía, la función debería devolver una lista vacía.
Su nombre debe ser mysplit().
"""


def mysplit(string:str):
    """
    Devuelve una lista de palabras a partir de una cadena, dividida por los 
    espacios en blanco.

    Args: 
        string (str): es la cadena de donde se va a crear la lista-
    """
    
    # Eliminar los espacios en blanco de la izquierda y de la derecha.
    string = string.strip()
    my_list = []   

    # Si la cadena no tiene nada, devolver la lista vacía.
    if not string:
        return my_list

    word = ""
    # Recorrer todos los caracteres de la cadena.
    for character in string:
        # Si no hay un espacio, formar la palabra
        if character != " ":
            word += character
        else:
            # Agregar la palabra a la lista y reiniciar la palabra.
            my_list.append(word)
            word = ""

    # Agregar la última palabra a la lista.
    my_list.append(word)
    
    return my_list


print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
