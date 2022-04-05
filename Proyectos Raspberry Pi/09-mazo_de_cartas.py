from carta import Carta
from mazo_de_cartas import Mazo

# El número de la carta va como texto porque en las cartas de poker hay
# también J, Q, K, A.
mi_carta = Carta("corazones", "6")
print(mi_carta)
#mi_carta.palo = "bastos"
# mi_carta.valor = -1
print(mi_carta)
mi_mazo = Mazo()
