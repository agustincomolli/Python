# Bucle for
print("Bucle 'for':\n" + "*" * 12)

for nombre in ["Agustín", "Lorena"]:
    print(nombre)

contados = ""
for i in range(9):
    contados += str(i + 1) + ", "
contados += "10"
print(f"Contar hasta diez: {contados}.")

# Bucle while
print("\nBucle 'while':\n" + "*" * 14)

numero = int(input("Ingrese un número: "))
suma = 0
while numero != 0:
    suma += numero
    print(f"Suma: {suma}")
    numero = int(input("Ingrese un número: "))
