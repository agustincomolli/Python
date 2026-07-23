# Crear una función que tome las 3 primeras letras de cada
# elemento de una lista y generar otra lista.
def acortar_nombre(nombre):
    return nombre[:3].upper()

equipos = ["Boca", "River", "Racing", "Independiente", "San Lorenzo"]
equipos_abr = []

for equipo in equipos:
    equipos_abr.append(acortar_nombre(equipo))

print(f"Equipos de la liga: {equipos_abr}")