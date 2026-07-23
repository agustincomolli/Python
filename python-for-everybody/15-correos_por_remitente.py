nombre_archivo = input("Ingrese el nombre del archivo: ")
correos = {}
max_cantidad = 0
max_remitente = ""

try:
    archivo = open(nombre_archivo, mode="r")
except:
    print("ERROR: El archivo no está disponible.")
    quit()

for linea in archivo:
    palabras = linea.split()
    if (len(palabras) == 0) or (palabras[0] != "From"):
        continue
    correos[palabras[1]] = correos.get(palabras[1], 0) + 1

archivo.close()
print("\nCorreos por usuario:", correos)

# for remitente, cantidad in correos.items():
#     if cantidad > max_cantidad:
#         max_cantidad = cantidad
#         max_remitente = remitente

lista = []
for remitente, cantidad in list(correos.items()):
    lista.append((cantidad, remitente))
lista.sort(reverse=True)
max_cantidad, max_remitente = lista[0]

print(f"\nUsuario con más correos: \"{max_remitente}\" con {max_cantidad} correos")
