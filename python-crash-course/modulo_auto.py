"""Una clase que se puede usar para representar un automóvil"."""

class Auto():
    """Representa un automóvil."""

    def __init__(self, fabricante, modelo, año) -> None:
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.lectura_kilometraje = 0

    
    def obtener_descripcion(self):
        """Devuelve un nombre descriptivo cuidadosamente formateado."""

        nombre_largo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_largo.title()


    def leer_cuentakilometros(self):
        """Imprime el kilometraje del auto."""

        print(f"Este auto tiene hechos {self.lectura_kilometraje} kilometros.")


    def actualizar_cuentakilometros(self, kilometraje):
        """
        Establecer el cuentakilometros en el valor dado.
        Rechazar el cambio si se intenta hacer retroceder el cuentakilometros.
        """
        if self.lectura_kilometraje < kilometraje:
            self.lectura_kilometraje = kilometraje
        else:
            print("No puedes retroceder el cuentakilómetros.")
    

    def incrementar_cuentakilometros(self, kilometros):
        """Suma la cantidad dada a la lectura del cuentakilómetros."""

        self.lectura_kilometraje += kilometros


    def llenar_tanque_combustible(self):
        """Muestra un mensaje diciendo que el tanque está lleno."""
        print("Se ha llenado el tanque de combustible.")