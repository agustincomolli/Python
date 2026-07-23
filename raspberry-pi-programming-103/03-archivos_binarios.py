# Crear un archivo en formato binario.
def crear_archivo():
    datos = [100,24,255]
    buffer = bytes(datos)
    print(f"- Lista en decimal: {datos}.\n- Lista en binario: {buffer}")
    f = open("binario.txt", "bw")
    f.write(buffer)
    print("Archivo binario creado.\n")
    f.close()

# Leer un archivo en formato binario.
def leer_archivo():
    f = open("binario.txt", "br")
    binario = f.read()
    datos = list(binario)
    print(f"- Lista en binario: {binario}.\n- Lista en decimal {datos}")
    f.close()

crear_archivo()
leer_archivo()