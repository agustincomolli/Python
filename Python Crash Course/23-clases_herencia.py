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


tesla = AutoElectrico("tesla", "modelo s", "2016")
print(tesla.obtener_descripcion())
tesla.bateria.describir_bateria()
tesla.llenar_tanque_combustible()
tesla.bateria.obtener_autonomia()
tesla.bateria.actualizar_bateria()
print(f"La nueva medida de la batería es de: {tesla.bateria.medida_bateria}")