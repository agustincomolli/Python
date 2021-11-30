from datetime import datetime

# Imprimir la hora actual y un mensaje en la pantalla.
def imprimir_hora(mensaje="Hora actual"):
    hora = datetime.now().time()
    # Formato de la hora: %I es la hora en formato de 12 horas
    #   %M minutos, %S segundos %p muestra AM o PM.
    hora = hora.strftime("%I:%M:%S %p")
    print(mensaje)
    print(hora)
    print()

# imprimir_hora("Bucle \"For\" iniciado.")
imprimir_hora()

for i in range(10):
    print(i)

imprimir_hora("\nBucle \"For\" terminado.")

input("Presione ENTER para continuar...")

# Obtener la letra inicial de un nombre o apellido.
# Devolver la inicial en mayúscula.
def obtener_inicial(nombre):
    inicial = nombre[0].upper()
    return inicial

nombre = input("\nEscriba su nombre: ")
apellido = input("Escriba su apellido: ")
print(f"Sus iniciales son {obtener_inicial(nombre)}. {obtener_inicial(apellido)}.\n")