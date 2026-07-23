def formatear_nombre(nombre, apellido, segundo_nombre=""):
    """Devuelve el nombre formateado."""
    if segundo_nombre:
        nombre_completo = f"{nombre} {segundo_nombre} {apellido}"
    else:
        nombre_completo = f"{nombre} {apellido}"
    return nombre_completo.title()

nombre = formatear_nombre("carlos", "gardel")
print(nombre)
nombre = formatear_nombre("agustín", "comolli", "alfredo")
print(nombre)

def crear_persona(nombre, apellido, edad=""):
    """Devuelve un diccionario con la información de una persona."""
    persona = {"nombre" : nombre, "apellido" : apellido}
    if edad:
        persona["edad"] = edad
    return persona

musico = crear_persona("Carlos", "Gardel", edad=27)
print(musico)

# Bucle infinito.
while True:
    nombre = input("\nIngrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nombre_completo = formatear_nombre(nombre, apellido)
    print(f"\n¡Hola {nombre_completo}!")
    if input("\n¿Desea continuar? [s|n]: ") == "n":
        break