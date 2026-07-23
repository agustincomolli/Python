def hacer_pizza(tamaño, *ingredientes):
    """Mostrar la pizza que estamos por hacer."""
    print(f"Haciendo una pizza {tamaño} con los siguientes ingredientes: ")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")