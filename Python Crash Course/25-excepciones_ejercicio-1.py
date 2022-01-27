# 10-6. Adición: un problema común cuando se solicita una entrada numérica 
# ocurre cuando las personas proporcionan texto en lugar de números. Cuando 
# intente convertir la entrada a un int, obtendrá un TypeError. Escriba un 
# programa que solicite dos números. Súmalos e imprime el resultado. Detecte 
# TypeError si alguno de los valores de entrada no es un número e imprima un 
# mensaje de error amigable. Pruebe su programa ingresando dos números y 
# luego ingresando algún texto en lugar de un número.

# 10-7. Calculadora de sumas: Envuelva su código del Ejercicio 10-6 en un 
# ciclo while para que el usuario pueda continuar ingresando números incluso 
# si comete un error e ingresa texto en lugar de un número.

# 10-8. Perros y gatos: haga dos archivos, cats.txt y dogs.txt. Guarde al 
# menos tres nombres de gatos en el primer archivo y tres nombres de perros 
# en el segundo archivo. Escriba un programa que intente leer estos archivos 
# e imprima el contenido del archivo en la pantalla. Envuelva su código en
# un bloque try-except para detectar el error FileNotFound e imprima un 
# mensaje amigable si falta un archivo. Mueva uno de los archivos a una 
# ubicación diferente en su sistema y asegúrese de que el código en el bloque 
# excepto se ejecute correctamente.

# 10-9. Gatos y perros silenciosos: modifique su bloque de excepción en el 
# ejercicio 10-8 para fallar silenciosamente si falta algún archivo.

# 10-10. Palabras comunes: Visite Project Gutenberg (http://gutenberg.org/ ) 
# y encuentre algunos textos que le gustaría analizar. Descargue los archivos 
# de texto de estos trabajos o copie el texto sin formato de su navegador a 
# un archivo de texto en su computadora.
# Puede usar el método count() para averiguar cuántas veces aparece una 
# palabra o frase en una cadena. Por ejemplo, el siguiente código cuenta el 
# número de veces que aparece 'rema' en una cadena:
# >>> linea = "Rema, rema, rema tu bote"
# >>> linea.contar('rema')
# 2
# >>> linea.lower().cuenta('rema')
# 3
# Tenga en cuenta que convertir la cadena a minúsculas usando lower() captura 
# todas las apariencias de la palabra que está buscando, independientemente 
# de cómo esté formateada.
# Escriba un programa que lea los archivos que encontró en el Proyecto 
# Gutenberg y determine cuántas veces aparece la palabra 'el' en cada texto.


from inspect import ArgSpec


print("Ejercicio 10-6 y 10-7\n" + "*" * 22)

continuar = "s"

while continuar == "s":
    try:
        numero_1 = int(input("Ingrese un número: "))
        numero_2 = int(input("Ingrese otro número: "))
    except ValueError:
        print("Debe ingresar un valor numérico.")
    else:
        print(f"La suma de los números ingresados es {numero_1 + numero_2}.")
        continuar = input("¿Desea continuar sumando? [s - continuar]: ").lower()
        print()


print("Ejercicio 10-8 y 10-9\n" + "*" * 22)

archivos = ["25-ejercicio-1_gatos.txt", "25-ejercicio-1_perros.txt"]

for archivo in archivos:
    
    # print(f"\nArchivo '{archivo}':")

    try:
        with open(archivo, "r", encoding="utf8") as lector_archivo:
            contenido = lector_archivo.read()
    except FileNotFoundError:
       # print("El archivo no existe.")
       pass
    else:
        print(f"Archivo '{archivo}':")
        print(contenido + "\n")
    

print("Ejercicio 10-10\n" + "*" * 15)

def contar_palabras(palabra):
    """Cuenta la cantidad de veces que se repite 'palabra'."""

    nombre_archivo = "25-moby_dick.txt"

    try:
        with open(nombre_archivo, "r", encoding="utf8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("No se encontró el archivo en la ubicación actual.")
    else:
        return contenido.lower().count(palabra)


palabra = "the"
cantidad = contar_palabras(palabra)
print(f"El libro Moby Dick tiene la palabra '{palabra}' " + \
    f"repetida {cantidad} veces.")