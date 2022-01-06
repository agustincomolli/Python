# 8-6. Nombres de ciudades: escriba una función llamada city_country () que 
# tome el nombre de una ciudad y su país. La función debería devolver una 
# cadena con el siguiente formato: "Santiago, Chile"
# Llame a su función con al menos tres pares de ciudad-país e imprima el 
# valor devuelto.

# 8-7. Álbum: escriba una función llamada make_album () que construya un 
# diccionario que describa un álbum de música. La función debe incluir un 
# nombre de artista y un título de álbum, y debe devolver un diccionario que 
# contenga estos dos datos. Utilice la función para crear tres diccionarios 
# que representen álbumes diferentes. Imprima cada valor de retorno para 
# mostrar que los diccionarios están almacenando la información del álbum 
# correctamente.
# Agregue un parámetro opcional a make_album () que le permita almacenar la 
# cantidad de pistas en un álbum. Si la línea de llamada incluye un valor 
# para la cantidad de pistas, agregue ese valor al diccionario del álbum. 
# Realice al menos una nueva llamada de función que incluya el número de 
# pistas de un álbum.

# 8-8. Álbumes de usuario: comience con su programa del ejercicio 8-7. 
# Escribe un bucle while que permita a los usuarios ingresar el artista y 
# el título de un álbum. Una vez que tenga esa información, llame a 
# make_album () con la entrada del usuario e imprima el diccionario 
# que se creó. Asegúrese de incluir un valor de salida en el ciclo while.

print("Ejercicio 8-6\n" + "*" * 14)

def ciudad_pais(ciudad, pais):
    """Devuelve la ciudad y el país correctamente formateados."""
    return f"{ciudad.title()}, {pais.title()}"

resultado = ciudad_pais("cañuelas", "argentina")
print(resultado)
resultado = ciudad_pais("pamplona", "españa")
print(resultado)
resultado = ciudad_pais("buenos aires", "argentina")
print(resultado)

print("\nEjercicio 8-7\n" + "*" * 14)

def hacer_album(artista, titulo_album, pistas=""):
    """Devuelve un diccionario con la información del album musical."""
    album = {"artista" : artista, "título" : titulo_album}
    if pistas:
        album["pistas"] = pistas
    return album

piano_guys = hacer_album("the piano guys", "ten")
print(piano_guys)
pearl_jam = hacer_album("pearl jam", "yield", 13)
print(pearl_jam)
luar_na_lubre = hacer_album("luar na lubre", "mar maior")
print(luar_na_lubre)

print("\nEjercicio 8-8\n" + "*" * 14)

while True:
    nuevo_artista = input("Ingrese el nombre del artista: ")
    nuevo_titulo = input("Ingrese el título del album: ")
    nuevo_album = hacer_album(nuevo_artista, nuevo_titulo)
    print(nuevo_album)
    if input("¿Desea continuar? [s|n]: ") == "n":
        break