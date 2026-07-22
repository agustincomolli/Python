"""
Ejemplo de bucles para iterar en listas.
Uso de in o not in para saber si hay o no hay un elemento en una lista.
"""

supplies = ["lápices", "gomas de borrar", "agendas", "reglas", "bolígrafos"]

for i in range(len(supplies)):
    print("Indice", str(i), "en suministros es:", supplies[i])


if "lápices" in supplies:
    print("¡Tenémos lápices para usted!")

if "compaces" not in supplies:
    print("Lamentablemente no tenemos compaces por el momento.")
