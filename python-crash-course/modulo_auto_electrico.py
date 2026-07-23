"""Un conjunto de clases que se pueden utilizar para representar coches eléctricos."""

from modulo_auto import Auto

class Bateria():
    """Modelo de batería de un auto eléctrico."""

    def __init__(self, medida_bateria = 70) -> None:
        """Inicializar atributos de la batería."""
        self.medida_bateria = medida_bateria


    def describir_bateria(self):
        """Imprime un mensaje describiendo la medida de la batería."""
        print(f"Este auto tiene una batería de {self.medida_bateria}-KWh.")


    def obtener_autonomia(self):
        """Muestra un mensaje de cuantos km puede hacer el auto 
        con esa batería."""
        if self.medida_bateria == 70:
            autonomia = 240
        elif self.medida_bateria == 80:
            autonomia = 270
        
        mensaje = f"Este auto puede hacer {autonomia} km con la " + \
                "batería completa."
        print(mensaje)


    def actualizar_bateria(self):
        """Establece en 85 la medida de la batería."""
        if self.medida_bateria != 85:
            self.medida_bateria = 85


# Herencia.
class AutoElectrico(Auto):
    """Representan aspectos de un automóvil, específicos de vehículos 
        eléctricos."""

    def __init__(self, fabricante, modelo, año) -> None:
        super().__init__(fabricante, modelo, año)
        # Clase como atributo.
        self.bateria = Bateria()
    
    # Sobreescribir métodos.
    def llenar_tanque_combustible(self):
        """Los autos eléctricos no tienen tanque de combustible."""
        print("Este auto no necesita un tanque de combustible.")