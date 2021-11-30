def crear_baraja():
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "As"]
    baraja = []

    for palo in palos:
        for carta in cartas:
            baraja.append(f"{carta} de {palo}")
    
    return baraja