# Abrir un archivo en modo append para agregar y no sobreescribir
#  datos. Se codifica el archivo para soportar caracteres internacionales.
archivo = open("nombres.txt", mode="a", encoding="utf-8")

nombre = input("Bienvenido ¿Cuál es tu nombre? ")
print("¡Hola " + nombre + " mucho gusto!")

# Escribir la información en el archivo.
archivo.write(nombre + "\n")
# Cerrar el archivo
archivo.close()