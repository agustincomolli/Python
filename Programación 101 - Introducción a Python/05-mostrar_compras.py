compras = ["pan", "queso", "manzanas", "tomates", "galletitas"]
contador = 0
for item in compras:
    contador += 1
    print(contador, " - ", item)

print(f"Tiene {len(compras)} artículos en su lista de compras")