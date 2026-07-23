autos = ["ford", "chevrolet", "fiat", "ferrari", "bmw", "alpha romeo", "pichistrili", "pindonga"]
print("Lista de autos:")

for auto in autos:
    # Si el auto es bmw, mostrar en mayúsculas.
    if auto == "bmw":
        print(auto.upper())
    else:
        print(auto.title())

# Verificar si un item no está en la lista.
if not "volkswagen" in autos:
    print("\nVolkswagen no están en la lista de los autos.\n")

# Según la marca de auto, indicar el origen de la misma.
for auto in autos:
    if auto == "fiat" or auto == "ferrari" or auto == "alpha romeo":
        print(auto.title() + " es una marca de autos italina.")
    elif auto == "chevrolet" or auto == "ford":
        print(auto.title() + " es una marca de autos de Estados Unidos.")
    elif auto == "bmw":
        print(auto.upper() + " es una marca de autos alemana.")
    else:
        print(auto.title(), " es una marca de autos desconocida.")