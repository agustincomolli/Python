prompt = "\nDime algo, y luego lo repetiré para ti. "
prompt += "\nEscriba 'salir' para salir del programa: "

activado = True
while activado:
    mensaje = input(prompt)
    if mensaje == "salir":
        activado = False
    else:
        print(f"Has dicho '{mensaje}'")

print("\n¡Bueno chau andate!")

print("\nContando impares...")
numero_actual = 0
while numero_actual < 10:
    numero_actual += 1
    if numero_actual % 2 == 0:
        continue

    print(numero_actual)