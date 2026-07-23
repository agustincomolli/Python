# Similar el lance de una moneda al aire y mostrar cual cara
# de la moneda salió.
moneda = ["cara", "cruz"]

# Seleccionar de forma aleatoria un item de la lista moneda.
def tirar_moneda():
    # Importar función de la librería random.
    from random import choice
    # Imprimir la cara de la moneda.
    print("La moneda cayó en", choice(moneda))

tirar_moneda()