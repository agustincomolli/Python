print("Primera parte:\n**************")
lecciones = ["Por qué programar en Python", "Tipos de datos y operadores", 
            "Flujo de control", "Funciones", "Scripting"]


def mi_enumerate(iterable, start=0):
    # Implemente su función de generador aquí
    contador = start
    for elemento in iterable:
        yield contador, elemento
        contador += 1

for i, leccion in mi_enumerate(lecciones, 1):
    print("Lección {}: {}".format(i, leccion))

print("\nSegunda parte:\n**************")


def chunker(iterable, tamaño):
    # Implementar la función aquí
    # inicio = 0
    # fin = tamaño
    # while inicio < len(iterable):
    #     yield iterable[inicio:fin]
    #     inicio += tamaño
    #     fin += tamaño
    for contador in range(0, len(iterable), tamaño):
        yield iterable[contador:contador+tamaño]


for chunk in chunker(range(25), 4):
    print(list(chunk))