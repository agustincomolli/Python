# Calcular la tasa de impuestos de Canadá
pais = input("\nIngrese el nombre de su país: ")
if pais.lower() == "canada":
    provincia = input("Ingrese el nombre de su provincia: ")
    if provincia.capitalize() in ("Alberta", "Nunavut", "Yukon"):
        impuestos = 0.05
    elif provincia.capitalize() == "Ontario":
        impuestos = 0.13
    else:
        impuestos = 0.15
else:
    print("No eres de Canadá.\n")
    impuestos = 0

print(f"La tasa de impuesto es de {impuestos}")
