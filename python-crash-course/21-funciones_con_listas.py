def saludo(nombres):
    """Imprime un saludo a cada nombre de la lista."""
    for nombre in nombres:
        print(f"¡Hola {nombre.title()} bienvenido!")

usuarios = ["adrián", "agustín", "carlitos"]
saludo(usuarios)

# Caso de ejemplo: Empresa que hace impresiones 3D.
def imprimir_modelos(diseños_a_imprimir, diseños_completados):
    """
    Simula la impresión de cada diseño hasta que no quede ninguno.
    Mueve cada diseño a la lista diseños_completados después de cada impresión.
    """
    while diseños_a_imprimir:
        diseño_actual = diseños_a_imprimir.pop()
        # Simula la impresión del modelo en 3D a partir del diseño.
        print(f"Imprimiendo el modelo {diseño_actual}")
        diseños_completados.append(diseño_actual)

def mostrar_diseños_completados(diseños_completados):
    """Muestra todos los diseños que se han impreso."""
    print("\nLos siguientes diseños se han impreso.")
    for diseño in diseños_completados:
        print(diseño)

diseños_a_imprimir = ["carcasa iphone", "robot", "dodecaedro"]
diseños_completados = []
print("\nDiseños 3D")
imprimir_modelos(diseños_a_imprimir, diseños_completados)
mostrar_diseños_completados(diseños_completados)