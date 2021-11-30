import string

print("Bienvenido al contador de letras\n" + ("=" * 32))
nombre_archivo = input("Ingrese el nombre del archivo: ")

letras = {}
otros_caracteres = string.punctuation + string.digits

try:
    archivo = open(nombre_archivo, mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

for linea in archivo:
    linea = linea.lower()
    for letra in linea:
        if letra in string.ascii_lowercase:
            letras[letra] = letras.get(letra, 0) + 1
archivo.close()

lista = []
for letra, cantidad in list(letras.items()):
    lista.append((cantidad, letra))
lista.sort(reverse=True)
for cantidad, letra in lista:
    print(f"Letra \"{letra}: {cantidad} veces.")