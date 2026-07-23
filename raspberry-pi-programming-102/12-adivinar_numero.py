## Juego de adivinanzas

max = 101
min = 0
respuesta = ""
contador = 0

def calcular_medio(minimo, maximo):
    return int((maximo + minimo) / 2)

print("Piense en un número entre 1 y 100")
while respuesta != "I":
    contador += 1
    medio = calcular_medio(min, max)
    respuesta = input(f"¿Es su número más [A]lto, más [B]ajo o es [I]gual que {medio}? ").upper()
    if respuesta == "A":
        min = medio
    elif respuesta == "B":
        max = medio
    else:
        if contador > 1:
            print(f"\nTu número es {medio}, me tomó {contador} veces adivinar")
        else:
            print(f"\nTu número es {medio}, me tomó {contador} vez adivinar")
        quit()
