from random import randint

# Crear una lista con los resultados de las tiradas de dados.
def tirar_dado(cant_veces):
    lista = []
    for contador in range(cant_veces):
        # randint selecciona un valor aleatorio entre 1 y 6
        lista.append(randint(1, 6)) 
    return lista

# Contar cuantas veces apareció cada uno de los números del dado
# en la lista de apariciones
def contar_apariciones(lista):
    for cara_dado in range(1, 7):
        if lista.count(cara_dado) < 2:
            print(f"El número {cara_dado} apareció {lista.count(cara_dado)} vez.")
        else:
             print(f"El número {cara_dado} apareció {lista.count(cara_dado)} veces.")

        
cant_veces = int(input("¿Cuántas veces tiras el dado? "))
lista_dado = tirar_dado(cant_veces)
print(lista_dado)
contar_apariciones(lista_dado)