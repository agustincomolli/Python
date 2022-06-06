def imprimir_listado(items, ancho_izq, ancho_der):
    """Imprimir el diccionario con las alineaciones correspondientes."""

    items = dict(items)
    print("Listado para el picnic".center(ancho_der + ancho_izq, "-"))
    for item, cantidad in items.items():
        print(item.ljust(ancho_izq, ".") + str(cantidad).rjust(ancho_der))


picnic = {"sanguches": 4, "manzanas": 12, "tazas": 4, "galletitas": 8000}
imprimir_listado(picnic, 12, 5)
print()
imprimir_listado(picnic, 24, 6)

print("\n" + "***Eso es todo amigos***".strip("*"))