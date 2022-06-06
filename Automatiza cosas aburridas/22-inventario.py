def mostrar_inventario(inventario):
    """Muestra el inventario que tiene el usuario en el juego."""
    
    inventario = dict(inventario)
    total_items = 0
    print(f"Inventario:\n{'*' * 11}")
    for item, cantidad in inventario.items():
        print(f" - {item}: {cantidad}")
        total_items += cantidad
    print(f"Número total de items: {total_items}")


def agregar_items(inventario, nuevos_items):
    """Agrega items al inventario del jugador."""

    inventario = dict(inventario)
    nuevos_items = list(nuevos_items)
    for item in nuevos_items:
        inventario.setdefault(item, 0)
        inventario[item] += 1
    return inventario


inventario = {"cuerda": 1, "antorcha": 6, "moneda de oro": 42, "daga": 1, 
    "flecha": 12}
mostrar_inventario(inventario)

botin_dragon = ["moneda de oro", "daga", "moneda de oro", "moneda de oro", "rubí"]
inventario = agregar_items(inventario, botin_dragon)
mostrar_inventario(inventario)