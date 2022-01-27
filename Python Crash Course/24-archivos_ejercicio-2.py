# 10-3. Invitado: escriba un programa que solicite al usuario su nombre. 
# Cuando respondan, escribe su nombre en un archivo llamado guest.txt.

# 10-4. Libro de invitados: escriba un bucle while que solicite a los 
# usuarios su nombre. Cuando ingresen su nombre, imprima un saludo en la 
# pantalla y agregue una línea que registre su visita en un archivo llamado 
# guest_book.txt. Asegúrese de que cada entrada aparezca en una nueva línea 
# en el archivo.

# 10-5. Encuesta de programación: escriba un ciclo while que pregunte a las 
# personas por qué les gusta programar. Cada vez que alguien ingrese un 
# motivo, agregue su motivo a un archivo que almacena todas las respuestas.

print("Ejercicio 10-3:\n" + "*" * 15)

nombre = input("Ingrese su nombre: ")

with open("24-invitados.txt", "w", encoding="UTF8") as archivo:
    archivo.write(nombre + "\n")


print("\nEjercicio 10-4:\n" + "*" * 15)

nombre = input("Ingrese su nombre: ").lower()

while nombre != "s":
    print(f"¡Hola {nombre.title()} bienvenido a mi programa!")

    with open("24-libro_visitas.txt", "a", encoding="UTF8") as archivo:
        archivo.write(nombre.title() + "\n")
        nombre = input("Ingrese su nombre: ").lower()


print("\nEjercicio 10-5:\n" + "*" * 15)

motivo = input("¿Por qué te gusta programar? [s = salir] ").lower()

while motivo != "s":
    with open("24-por_que_programar.txt", "a", encoding="UTF8") as archivo:
        archivo.write(motivo.capitalize() + "\n")
        motivo = input("¿Por qué te gusta programar? [s = salir] ").lower()
