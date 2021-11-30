# Mostrar la característica de combinación de la función format().
print("\nPaso 1: \n********")

medicamento = "Espectosan"
dosis = 5
duracion = 4.5

instrucciones = "{} - Tome {} ml por vía oral cada {} horas".format(medicamento, dosis, duracion)
print(instrucciones)

instrucciones = "{2} - Tome {1} ml por vía oral cada {0} horas.".format(medicamento, dosis, duracion)
print(instrucciones)

instrucciones = "{medicamento} - Tome {dosis} ml por vía oral cada {duracion} horas.".format(medicamento = "Pulmosan", dosis = 10, duracion = 6)
print(instrucciones)

# Usar literales de cadena con formato o "cadenas f".
print("\nPaso 2: \n********")

nombre = "Mundo"
mensaje = f"¡Hola, {nombre}!"

print(mensaje)

contar = 10
valor = 3.14
mensaje = f"Contar hasta {contar}. Multiplicar por {valor}"

print(mensaje)

# Evaluar expresiones simples en el campo de reemplazo de una cadena f.
print("\nPaso 3: \n********")

ancho = 5
alto = 10

print(f"El perímetro es de {(2 * ancho) + (2 * alto)} y el área es {ancho * alto}.")

# Definir especificadores de formato para controlar la alineación y el relleno.
print("\nPaso 4: \n********")

valor = "Hola"

print(f".{valor:<25}.")
print(f".{valor:>25}.")
print(f".{valor:^25}.")
print(f".{valor:-^25}.")