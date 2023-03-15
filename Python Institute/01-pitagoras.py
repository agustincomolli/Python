# Teorema de Pitágoras:
# El cuadrado de la hipotenusa es igual a la suma de los cuadrados de
# los dos catetos.

def get_hypotenuse(mayor: int, minor: int):
    """
    Description: Devuelve la hipotenusa usando el teorema de Pitágoras.
    Parameters:  - mayor: cateto mayor.
                 - minor: cateto menor.
    """
    hypotenuse = (mayor ** 2 + minor ** 2) ** 0.5

    return hypotenuse


mayor_side = int(input("Cateto mayor: "))
minor_side = int(input("Cateto menor: "))
hypotenuse = get_hypotenuse(mayor_side, minor_side)
print(f"La hipotenusa es {hypotenuse}")
