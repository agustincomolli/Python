# Crear una función pequeña y llamarla
print("\nPaso 1: \n********")

def decir_hola():
    print("¡Hola mundo!")

decir_hola()

# Crear una función pequeña y aceptar un parámetro de entrada
print("\nPaso 2: \n********")

def decir_hola(nombre):
    print(f"¡Hola {nombre}!")

decir_hola("Agustín")

# Llamar función para omitir el argumento
print("\nPaso 3: \n********")

def decir_hola(nombre = "mundo"):
    print(f"¡Hola {nombre}!")

decir_hola()
decir_hola("Agustín")

#  Incluir un segundo parámetro opcional de entrada
print("\nPaso 4: \n********")

def decir_hola(nombre = "mundo", saludo = None):
    if saludo == None:
        print(f"¡Hola {nombre}!")
    else:
        print(f"¡{saludo} {nombre}!")

decir_hola()
decir_hola("Agustín")
decir_hola(saludo="Qué tal")
decir_hola("Agustín", "Qué tal")

# Sumar dos números con una función
print("\nPaso 4: \n********")

def sumar_dos_numeros(x, y):
    return x + y

sumar_dos_numeros(4, 6)
resultado = sumar_dos_numeros(5, 7)
print(resultado)

# Devolver una lista en una función
print("\nPaso 5: \n********")

def crear_maso_de_cartas():
    palos_de_carta = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    numeros_de_carta = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "As"]
    maso_de_cartas = []

    for palo in palos_de_carta:
        for numero in numeros_de_carta:
            maso_de_cartas.append(f"{numero} de {palo}")

    return maso_de_cartas

mi_maso = crear_maso_de_cartas()
print(len(mi_maso))