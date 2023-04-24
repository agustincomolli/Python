"""
escribir una función capaz de ingresar valores enteros y verificar si están 
dentro de un rango especificado.

La función deberá:

- Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite 
superior aceptable.
- Si el usuario ingresa una cadena que no es un valor entero, la función debe 
emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que 
ingrese el valor nuevamente.
- Si el usuario ingresa un número que está fuera del rango especificado, la 
función debe emitir el mensaje Error: el valor no está dentro del rango 
permitido (min..max) y solicitará al usuario que ingrese el valor nuevamente.
- Si el valor de entrada es válido, será regresado como resultado.

"""


def read_int(prompt: str, min: int, max: int):
    """
    Devuelve un número entero ingresado por el usuario,comprendido entre el valor min y max.

    Args:
        prompt(str): Es el mensaje que se mostrará al usuario.
        min, max (int): Valores en los que se validará la entrada del usuario.

    """

    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Entrada incorrecta.")
        
        if number < min or number > max:
            print(
                f"El valor no está dentro del rango permitido (min = {min}, max = {max})")
        else:
            return number


v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)

print("El número es:", v)
