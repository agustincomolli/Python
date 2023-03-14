# Teorema de Pitágoras:
# El cuadrado de la hipotenusa es igual a la suma de los cuadrados de 
# los dos catetos.

def get_hypotenuse(mayor:int, minor:int):
    """
    Description: Devuelve la hipotenusa usando el teorema de Pitágoras.
    Parameters:  - mayor: cateto mayor.
                 - minor: cateto menor.
    """
    hypotenuse = (mayor ** 2 + minor ** 2) ** 0.5

    return hypotenuse

a = 3
b = 4
hypotenuse = get_hypotenuse(4,3)
print(f"La hipotenusa es {hypotenuse}")