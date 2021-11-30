def leer_archivo():
    # Abrir un archivo en modo lectura usando el método de
    # codificación para leer caracteres internacionales.
    print("\nAbrir archivo directo:")
    archivo = open("comida.txt", mode="r", encoding="utf-8")
    # Leer el contenido del archivo
    datos = archivo.read()
    print(datos)

def recorrer_archivo():
    # Recorrer el archivo línea a línea.
    print("\nRecorrer el archivo línea por línea:")
    archivo = open("comida.txt", mode="r", encoding="utf-8")
    for linea in archivo:
        print("- " + linea.strip())
    # Cerrar el archivo.
    archivo.close() 

def usar_with():
    # Abrir un archivo usando la declaración with.
    print("\nAbrir archivo con with: ")
    with open("comida.txt", mode="r", encoding="utf-8") as archivo:
        datos = archivo.read()
        print(datos)

leer_archivo()
recorrer_archivo()
usar_with()