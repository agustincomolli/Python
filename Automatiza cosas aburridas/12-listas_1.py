print("Ingrese los nombres de las mascotas, ingrese 's' para salir.")
mascota = input("Mascota: ")
lista_mascotas = []
while mascota != "s":
    if mascota != "":
        lista_mascotas += [mascota]
    mascota = input("Mascota: ")

print("\nListado de mascotas:")
for mascota in lista_mascotas:
    print(f"- {mascota}")

print("\nListado de mascotas numeradas:")
for i in range(len(lista_mascotas)):
    print(f"{i + 1} - {lista_mascotas[i]}")

if "Chingola" in lista_mascotas:
    print("\nLa Chingola está en la lista.")
if "Boluda" not in lista_mascotas:
    print("\nTe olvidaste de poner a la Boluda.")