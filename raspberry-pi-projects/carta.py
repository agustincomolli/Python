class Carta:
    """Modela una carta de poker."""

    def __init__(self, palo, numero, valor=1) -> None:
        """Inicializar el objeto carta."""
        self.palo = palo
        self.numero = numero
        self.valor = valor

    
    def __repr__(self) -> str:
        """Muestra el valor de la carta."""
        return f"{self._numero} de {self._palo}"

    
    # Getter para palo.
    @property
    def palo(self):
        return self._palo


    # Setter para palo.
    @palo.setter
    def palo(self, palo):
        if palo in ["corazones", "diamantes", "tréboles", "picas"]:
            self._palo = palo.title()
        else:
            raise ValueError(f"'{palo}' no es un conjunto de cartas de poker.")
    

    # Getter para numero.
    @property
    def numero(self):
        return self._numero

    
    # Setter para numero.
    @numero.setter
    def numero(self, numero):
        if numero in [
                        "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                        "J", "Q", "K", "As"
                    ]:
            self._numero = numero.title()
        else:
            raise ValueError(f"'{numero}' no es un valor correcto.")


    # Getter para valor.
    @property
    def valor(self):
        return self._valor


    # Setter para valor.
    @valor.setter
    def valor(self, valor):
        if int(valor) > 0:
            self._valor = int(valor)
        else:
            raise ValueError(f"{valor} no es válido. Debe ingresar un " +
                "número entero mayor a 0")