# Convertir una temperatura medida en grados Fahrenheit a una temperatura 
# medida en grados Celsius. (celsius = (fahrenheit - 32) * 5/9)
fahrenheit = input("¿Cuál es la temperatura en grados Fahrenheit?")

if fahrenheit.isnumeric() == False:
    print("La entrada no es un número.")
    exit()

fahrenheit = int(fahrenheit)
celsius = int((fahrenheit - 32) * 5/9)

print(f"La temperatura en grados Celsius es {celsius}")