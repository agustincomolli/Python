from mylib import *


def cipher_cesar(text: str) -> str:
    """
    Devuelve una cadena cifrada en la que las letras del texto ingresado se
    reemplazan con su consecuente más cercano.

    Args:
        text (str): Texto ingresado por el usuario que desea cifrar.

    """

    text = text.upper()
    cipher = ""

    for letter in text:
        if letter == "Z":
            letter = "A"
        elif letter.isalpha():
            code = ord(letter)
            letter = chr(code + 1)
        cipher += letter

    return cipher


def decipher_cesar(cipher_text: str) -> str:
    """
    Devuelve una cadena con el texto decifrado.

    Args:
        cipher_text (str): Contiene el mensaje cifrado con el método Cesar.

    """

    decipher = ""
    
    for letter in cipher_text:
        if letter == "A":
            letter = "Z"
        elif letter.isalpha():
            code = ord(letter)
            letter = chr(code - 1)
        decipher += letter

    return decipher


secret = input_color("Ingrese el texto a cifrar: ", "green")
secret = cipher_cesar(secret)
print(secret)
print("\n" + decipher_cesar(secret))
