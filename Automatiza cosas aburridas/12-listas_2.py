import random

lista_mascotas = ["Chingola", "Pancha", "Vidú", 
    "Boluda", "Mendieta", "Pocholo"]

print("Listado de mascotas:\n")
# Usar la función enumerate().
for indice, mascota in enumerate(lista_mascotas):
    print(f"{indice + 1} - {mascota}")

print(f"\nElegir una mascota al azar: '{random.choice(lista_mascotas)}'")

print("\nLista reordenada aleatoriamente: ")
random.shuffle(lista_mascotas)
print(lista_mascotas)