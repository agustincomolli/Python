# 8-9. Magos: haz una lista de nombres de magos. Pase la lista a una función 
# llamada show_magicians (), que imprime el nombre de cada mago en la lista.

# 8-10. Grandes magos: comience con una copia de su programa del 
# ejercicio 8-9. Escribe una función llamada make_great () que modifique la 
# lista de magos agregando la frase Great al nombre de cada mago. Llame a 
# show_magicians () para ver que la lista ha sido modificada.

# 8-11. Magos sin cambios: comience con su trabajo del ejercicio 8-10. Llame 
# a la función make_great () con una copia de la lista de nombres de magos. 
# Debido a que la lista original no se modificará, devuelva la nueva lista 
# y guárdela en una lista separada. Llame a show_magicians () con cada lista 
# para mostrar que tiene una lista de los nombres originales y una lista con 
# el Great agregado al nombre de cada mago.

print("Ejercicio 8-9: \n" + "*" * 14)

def mostrar_magos(lista_magos):
    """Muestra la lista de magos."""
    for mago in lista_magos:
        print(mago.title())

magos = ["harry potter", "hermione", "ron", "dumbledore"]
mostrar_magos(magos)

print("\nEjercicio 8-10: \n" + "*" * 15)

def hacer_grande(lista_magos):
    """Agrega sufijo 'Gran' al nombre del mago y devuelve una nueva lista."""
    copia_lista = lista_magos[:]
    for i in range(len(copia_lista)):
        copia_lista[i] = "gran " + copia_lista[i]
    return copia_lista

grandes_magos = hacer_grande(magos)
mostrar_magos(magos)
mostrar_magos(grandes_magos)
