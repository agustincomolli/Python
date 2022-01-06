# Coche de alquiler: escriba un programa que le pregunte al usuario qué tipo 
# de coche de alquiler le gustaría. Imprime un mensaje sobre ese coche, como 
# "Déjame ver si puedo buscarte un Subaru".
auto = input("¿Qué tipo de auto le gustaría alquilar? ")
print(f"Déjame ver si puedo buscarte un {auto}.")

# Asientos en el restaurante: escriba un programa que pregunte al usuario 
# cuántas personas hay en su grupo de cena. Si la respuesta es más de ocho, 
# imprima un mensaje que diga que tendrán que esperar por una mesa. De lo 
# contrario, informe que su mesa está lista.
grupo = int(input("\n¿Cuántas personas van a cenar? "))
if grupo > 8:
    print("Tendrán que esperar por una mesa.")
else:
    print("Su mesa está lista.")

# Múltiplos de diez: pida al usuario un número y luego informe si el número 
# es múltiplo de 10 o no.
numero = int(input("\nIngrese un número: "))
if numero % 10 == 0:
    print(f"El número {numero} es múltiplo de 10.")
else:
    print(f"El número {numero} no es múltiplo de 10.")