from random import randint

def fusion(lista_a, lista_b):
    lista_ordenada = []
    # Mientras las listas contengan algún valor...
    while len(lista_a) > 0 and len(lista_b) > 0:
        # Si una valor es más chico que otro,
        # agregarlo a la lista ordenada y borrarlo
        # de la lista de origen.
        if lista_a[0] < lista_b[0]:
            lista_ordenada.append(lista_a.pop(0))
        else:
            lista_ordenada.append(lista_b.pop(0))
    
    # Si la lista a no tiene elementos:
    if len(lista_a) < 1:
        # Agregar a la lista ordenada todos los elementos
        # restantes de la lista b.
        lista_ordenada += lista_b
    else:
        lista_ordenada += lista_a

    return lista_ordenada

# Ordenar una lista según el método de fusión.
def ordenar_fusion(lista_desordenada):
    # Si la lista tiene 1 o 0 elementos se la considera
    # ordenada.
    if len(lista_desordenada) <= 1:
        return lista_desordenada
    else:
        # Buscar el medio de la lista y redondearlo.
        medio = int(len(lista_desordenada) / 2)
        # Dividir la lista en dos y volver a llamar a la función
        # recursiva para dividir la lista hasta que quede un
        # elemento.
        lista_izq = ordenar_fusion(lista_desordenada[:medio])
        lista_der = ordenar_fusion(lista_desordenada[medio:])
    return fusion(lista_izq, lista_der)

desordenada = [randint(1, 20) for i in range(randint(5,20))]

print(f"Lista desordenada:\n {desordenada}\n")

print(f"Lista ordenada:\n {ordenar_fusion(desordenada)}")