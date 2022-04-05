from carta import Carta

class Mazo():
    """Modela un mazo de cartas."""

    def __init__(self) -> None:
        """Inicializar el mazo de cartas."""
        self._cartas = []
        self.llenar()
        print(self._cartas)

    
    def llenar(self):
        """Crear una lista de cartas con sus palos y números 
        correspondientes."""

        palos = ["corazones", "diamantes", "tréboles", "picas"]
        numeros = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "As"]
        
        # cartas = []
        # for palo in palos:
        #     for numero in numeros:
        #         cartas.append(Carta(palo, numero))
        
        # self._cartas = cartas

        # Usar comprensión de listas.
        self._cartas = [Carta(p,n) for p in palos for n in numeros]