# Diccionarios anidados.
invitados = {
    "alicia" : {"manzanas" : 5, "facturas" : 12},
    "bernardo" : {"sanguches" : 6, "manzanas" : 3},
    "luis" : {"tazas" : 3, "tarta de manzana" : 1}
    }

def calcular_traido(invitados, articulo):
    total = 0 
    for nombre, cosas in invitados.items():
        total += cosas.get(articulo, 0)
    return total


print("Cosas traídas:")
print(f" - Manzanas: {calcular_traido(invitados, 'manzanas')}")
print(f" - Tazas: {calcular_traido(invitados, 'tazas')}")
print(f" - Tortas: {calcular_traido(invitados, 'tortas')}")
print(f" - Sanguches: {calcular_traido(invitados, 'sanguches')}")
print(f" - Tartas de manzana: {calcular_traido(invitados, 'tarta de manzana')}")