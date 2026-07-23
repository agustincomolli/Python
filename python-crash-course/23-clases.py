class Perro():
    """Un simple intento de modelar un perro."""

    def __init__(self, nombre, edad) -> None:
        """Inicializar atributos nombre y edad."""
        self.nombre = nombre
        self.edad = edad

    def sentar(self):
        """Simule a un perro sentado en respuesta a una orden."""
        print(f"{self.nombre.title()} está sentado.")

    def rodar(self):
        """Simular volcarse en respuesta a un comando."""
        print(f"¡{self.nombre.title()} rodó!")


mi_perro = Perro("Mendieta", 14)

print(f"Mi perro se llama {mi_perro.nombre}.")
print(f"{mi_perro.nombre} tiene {mi_perro.edad} años.")
mi_perro.sentar()
mi_perro.rodar()
otro_perro = Perro("Mondiola", 3)
print(f"Tuve una perra que se llamaba {otro_perro.nombre} " + 
    f"y tenía {otro_perro.edad} años.")
