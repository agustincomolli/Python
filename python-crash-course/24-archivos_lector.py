# Leer todo un archivo e imprimir su contenido.
print("Leer todo un archivo:")
with open("24-archivos_pi.txt") as archivo:
    contenido = archivo.read()
    print(contenido)


# Leer un archivo línea por línea.
print("\nLeer un archivo línea por línea:")
nombre_archivo = "24-archivos_pi.txt"
with open(nombre_archivo) as archivo:
    for linea in archivo:
        # rstrip() elimina los saltos de línea.
        print(linea.rstrip())

# Hacer una lista con las líneas del archivo.
print("\nHacer una lista con las líneas del archivo:")
with open(nombre_archivo) as archivo:
    contenido = archivo.readlines()

for linea in contenido:
    print(linea.rstrip())


# Trabajar con el contenido del archivo.
print("\nTrabajar con el contenido del archivo.")
nombre_archivo = "24-archivos_pi.txt"
pi = ""

with open(nombre_archivo) as archivo:
    lineas_archivo = archivo.readlines()

for linea in lineas_archivo:
    # strip quita los espacios en blanco y saltos de línea.
    pi += linea.strip()

print(pi)


# Trabajar con un millón de dígitos.
print("\nTrabajar con un millón de dígitos.")
nombre_archivo = "24-pi_millon_digitos.txt"
pi = ""

with open(nombre_archivo) as archivo:
    lineas_archivo = archivo.readlines()

for linea in lineas_archivo:
    # strip quita los espacios en blanco y saltos de línea.
    pi += linea.strip()

print(pi[:52] + "...")


# Cumpleaños en pi.
print("\nCumpleaños en número pi:")
cumpleaños = input("Ingrese su fecha de nacimiento en formato ddmmaa: ")

nombre_archivo = "24-pi_millon_digitos.txt"
pi = ""

with open(nombre_archivo) as archivo:
    lineas_archivo = archivo.readlines()

for linea in lineas_archivo:
    # strip quita los espacios en blanco y saltos de línea.
    pi += linea.strip()

if cumpleaños in pi:
    print("¡Tu cumpleaños aparece en el millón de dígitos del número pi!")
else:
    print("Tu cumpleaños no aparece.    ='(")