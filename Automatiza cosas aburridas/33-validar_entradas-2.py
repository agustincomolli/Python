import pyinputplus as pyip

# Crear un función que sume los dígitos ingresados y devuelva True si suman 10.
def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    if suma != 10:
        raise Exception(f"La suma de los dígitos debe ser 10, no {suma}.")
    return int(numero)

respuesta = pyip.inputCustom(suma_digitos, 
                             prompt="Ingrese un número que sume 10: ",
                             allowRegexes=[r"[0-9]+"])

print(respuesta)