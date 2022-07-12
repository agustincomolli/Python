from pathlib import Path

def reemplazar_palabra(palabra: str(), reemplazo:str()):
    """Reemplazar el código por la opción del usuario."""

    # Si la palabra a reemplazar termina con un signo de puntuación...
    if palabra[-1] in [",",";",".",":","-"]:
        # Agregar el signo al final del reemplazo.
        reemplazo += palabra[-1]
    return reemplazo


def buscar_reemplazar(lista_palabras, reemplazar_palabra):
    """Buscar códigos para ser reemplazados por el usuario."""

    for indice, palabra in enumerate(lista_palabras):
        if palabra[:9] == "[adj-mas]":
            descripcion = "adjetivo masculino"
        elif palabra[:9] == "[adj-fem]":
            descripcion = "adjetivo femenino"
        elif palabra[:9] == "[sus-mas]":
            descripcion = "sustantivo masculino"
        elif palabra[:9] == "[sus-fem]":
            descripcion = "sustantivo femenino"
        elif palabra[:6] == "[verb]":
            descripcion = "verbo"
        else:
            continue
        cambio = input(f"Ingrese un {descripcion}: ")
        lista_palabras[indice] = reemplazar_palabra(palabra, cambio)


ruta_archivo = Path(Path.cwd() / "Automatiza cosas aburridas", "41-mathlibs.txt")
texto_final = ""

# Abrir archvio
archivo_mathlib = open(ruta_archivo, mode="r", encoding="UTF-8")
# Leer el  contenido por líneas.
for linea in archivo_mathlib.readlines():
    lista_palabras = linea.split()
    buscar_reemplazar(lista_palabras, reemplazar_palabra)
    texto_final += " ".join(lista_palabras) + "\n"
# Cerrar archivo.
archivo_mathlib.close()

print(f"\n{texto_final.rstrip()}")
