# Generar una lista con los resultados aleatorios
# que simulen los resultados de un examen.
def generar_calificaciones(cant_alumnos):
    from random import randint

    lista_calificaciones = []
    for i in range(cant_alumnos):
        lista_calificaciones.append(randint(1, 10))

    return lista_calificaciones

# Devolver la cantidad de veces que aparece un item en una lista.
def contar_item(item, lista):
    total = 0
    if not isinstance(item, list):
        item = [item]

    for elemento in lista:
        if elemento in item:
            total += 1

    return total

resultados_examen = generar_calificaciones(24)
print(f"Resultados de los exámenes: \n {resultados_examen}")
print(f"\nHay {contar_item(10, resultados_examen)} alumnos que se sacaron 10 en el examen.")

lista_cadena = ["té", "mate", "café", "mate","té", "mate"]
print(f"\nLista de infusiones bebidas en el día: {lista_cadena}")
print(f"Has tomado té {contar_item('té', lista_cadena)} veces en el día.")
palabra = "palabrerio sin acento"
vocales = ["a", "e", "i", "o", "u"]
print(f"\n'{palabra}' tiene {contar_item(vocales, palabra)} vocales.")