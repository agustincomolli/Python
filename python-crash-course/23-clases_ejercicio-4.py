# 6-3. Glosario: se puede usar un diccionario de Python para modelar un 
# diccionario real. Sin embargo, para evitar confusiones, llamémoslo glosario.
# • Piense en cinco palabras de programación que haya aprendido en los 
# capítulos anteriores. Utilice estas palabras como claves en su glosario y 
# almacene sus significados como valores.
# • Imprima cada palabra y su significado como una salida ordenada. Puede 
# imprimir la palabra seguida de dos puntos y luego su significado, o 
# imprimir la palabra en una línea y luego imprimir su significado con 
# sangría en una segunda línea. Utilice el carácter de nueva línea (\n) para 
# insertar una línea en blanco entre cada par de palabra y significado en su 
# salida.

# 6-4. Glosario 2: ahora que sabe cómo recorrer un diccionario, limpie el 
# código del ejercicio 6-3 (página 102) reemplazando su serie de 
# instrucciones de impresión con un ciclo que recorre las claves y los 
# valores del diccionario. Cuando esté seguro de que su ciclo funciona, 
# agregue cinco términos más de Python a su glosario. Cuando vuelva a 
# ejecutar su programa, estas nuevas palabras y significados deberían 
# incluirse automáticamente en la salida.

# 9-13. Reescritura de OrderedDict: comience con el ejercicio 6-4 
# (página 108), donde usó un diccionario estándar para representar un 
# glosario. Vuelva a escribir el programa usando la clase OrderedDict y 
# asegúrese de que el orden de la salida coincida con el orden en que se 
# agregaron los pares clave-valor al diccionario.

# 9-14. Dice: El módulo aleatorio contiene funciones que generan números 
# aleatorios de varias formas. La función randint() devuelve un número 
# entero en el rango que proporcione. El siguiente código devuelve un número 
# entre 1 y 6:
#     "from randint de import randint"
#     "x = randint(1, 6)"
# Crea un dado de clase con un atributo llamado lados, que tiene un valor 
# predeterminado de 6. Escribe un método llamado roll_die() que imprima un 
# número aleatorio entre 1 y el número de lados que tiene el dado. Haz un 
# dado de 6 caras y tíralo 10 veces.
# Haz un dado de 10 caras y un dado de 20 caras. Tira cada dado 10 veces.

# 9-15. Python Module of the Week: un excelente recurso para explorar la 
# biblioteca estándar de Python es un sitio llamado Python Module of the 
# Week. Vaya a http://pymotw.com/ y mire la tabla de contenido. Encuentre 
# un módulo que le parezca interesante y lea sobre él, o explore la 
# documentación de las colecciones y los módulos aleatorios.

from collections import OrderedDict

glosario = OrderedDict()

glosario["input"] = "La función input() permite introducir datos " + \
    "de distintos tipos desde un teclado."
glosario["if"] = "Se utiliza para ejecutar un bloque de código si, " + \
    "y solo si, se cumple una determinada condición."
glosario["for"] = "Se utiliza para recorrer los elementos de un " + \
    "objeto iterable (lista, tupla, conjunto, diccionario, …) y " + \
    "ejecutar un bloque de código."
glosario["while"] = "Permite ejecutar ciclos, o bien secuencias " + \
    "periódicas que nos permiten ejecutar código múltiples veces."
glosario["print"] = "Permite imprimir una cadena de texto en la pantalla."
glosario["def"] = "Permite definir un bloque de código " + \
    "reutilizable que se puede ejecutar muchas veces dentro de tu programa."
glosario["class"] = "Plantilla o modelo a partir de la cual podemos " + \
    "crear objetos y donde se determinan los atributos (características) " + \
    "y métodos (acciones realizables) que tendrán."
glosario["list"] = "Permite almacenar conjuntos de elementos " + \
    "relacionados del mismo tipo o de tipos distintos."
glosario["str"] = "Tipo de dato que se utiliza para representar texto."
glosario["int"] = "Tipo de dato que se utiliza para representar " + \
    "número enteros."

print("Diccionario de Python\n" + "*" * 21)
for clave, valor in glosario.items():
    print(f"{clave}: \n  - {valor}")

print("\nEjercicio 9-14\n" + "*" * 14)

from random import randint

class Dado():
    """Modela un dado."""

    def __init__(self, caras) -> None:
        """Inicializar atributos."""
        self.caras = caras


    def tirar_dado(self):
        return randint(1, self.caras)


mi_dado = Dado(6)
resultado = ""
for i in range(10):
    resultado += str(mi_dado.tirar_dado()) + " "

print(resultado)

mi_dado = Dado(10)
resultado = ""
for i in range(20):
    resultado += str(mi_dado.tirar_dado()) + " "

print(resultado)