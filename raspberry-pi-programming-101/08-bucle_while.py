adivina = input("Adivina mi nombre: ")
intentos = 1
while adivina != "Agustín":
    adivina = input("¡No! Prueba de nuevo: ")
    intentos += 1

print(f"¡Bien hecho! Lo conseguiste en {intentos} intento(s)")