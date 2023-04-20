"""
Un número de cuenta compatible con IBAN consta de:

- Un código de país de dos letras tomado del estándar ISO 3166-1 (por ejemplo, 
FR para Francia, GB para Gran Bretaña DE para Alemania, y así sucesivamente).
- Dos dígitos de verificación utilizados para realizar las verificaciones de 
validez: pruebas rápidas y simples, pero no totalmente confiables, que 
muestran si un número es inválido (distorsionado por un error tipográfico) o 
válido.
- El número de cuenta real (hasta 30 caracteres alfanuméricos; la longitud de 
esa parte depende del país).
- El estándar dice que la validación requiere los siguientes pasos (según 
Wikipedia):

(Paso 1) Verificar que la longitud total del IBAN sea correcta según el país 
(este programa no lo hará, pero puedes modificar el código para cumplir con 
este requisito si lo deseas; nota: pero debes enseñar al código a conocer 
todas las longitudes utilizadas en Europa).
(Paso 2) Mueve los cuatro caracteres iniciales al final de la cadena (es 
decir, el código del país y los dígitos de verificación).
(Paso 3) Reemplaza cada letra en la cadena con dos dígitos, expandiendo así 
la cadena, donde A = 10, B = 11 ... Z = 35.
(Paso 4) Interpreta la cadena como un entero decimal y calcula el residuo de 
ese número dividiéndolo entre 97. Si el residuo es 1, pasa la prueba de 
verificación de dígitos y el IBAN puede ser válido.
"""

from mylib import *


def validate_iban(iban: str) -> bool:
    """
    Devuelve True si el parámetro iban cumple con los requisitos para ser un
    código IBAN correcto.

    Args:
        iban (str): Es el código que se quiere verificar.
    """

    # Quitar los espacios en blanco.
    iban = iban.replace(" ", "")
    # Verificar que solo haya números y letras.
    if not iban.isalnum():
        raise ValueError("Has introducido caracteres inválidos.")
    elif len(iban) < 15 or len(iban) > 30:
        raise ValueError(
            "El código IBAN no tiene la cantidad de dígitos requeridos.")
    else:
        # Poner las letras en mayúsculas.
        iban = iban.upper()
        # Trasladar los 4 primeros caracteres al final de la cadena.
        iban = iban[4:] + iban[:4]

        verifiation_code = ""
        # Reemplazar cada letra en la cadena con dos dígitos, expandiendo así 
        # la cadena, donde A = 10, B = 11 ... Z = 35.
        for character in iban:
            if character.isdigit():
                verifiation_code += character
            else:
                verifiation_code += str(10 + ord(character) - ord("A"))

        verifiation_code = int(verifiation_code)
        # Calcular si residuo de ese número dividiéndolo entre 97 es igual a 1.
        if verifiation_code % 97 == 1:
            return True
        else:
            return False


clear_screen()
print(color_me("💰 International Bank Account Number 💰\n", "yellow"))

iban = input_color("Ingrese un IBAN: ", "green")
try:
    if validate_iban(iban):
        print("\nEl IBAN parece correcto. ✔️")
    else:
        print("\nEl código IBAN no ha pasado la verificación. ✖️")
except ValueError as error:
    show_error(str(error))
