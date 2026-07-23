import string

dic_palabras = {}

try:
    archivo = open("words.txt", mode="r")
except:
    print("ERROR: El archivo no está disponible.")
    quit()

for linea in archivo:
    # Borrar los caracteres en blanco del final de la línea.
    linea = linea.rstrip()
    # Crear una nueva línea sin los caracteres de puntuación.
    linea = linea.translate(linea.maketrans("","", string.punctuation))
    linea = linea.lower()
    palabras = linea.split()
    for palabra in palabras:
        # El método get devuelve el valor del diccionario y si no existe
        # devuelve un valor predeterminado.
        dic_palabras[palabra] = dic_palabras.get(palabra,0) + 1

archivo.close()
print("Histograma:\n" + ("=" * 11))
print(dic_palabras)
# Ordenar el diccionario por valor.
lista = []
for clave, valor in list(dic_palabras.items()):
    lista.append((valor, clave))

lista.sort(reverse=True)

print("\nLas 10 palabras más comunes son:\n" + ("=" * 32))
for valor, clave in lista[:10]:
    print("La palabra", "\"" + clave + "\"", "aparece", valor, "veces")