print("Ingrese tres números para calcular la fórmula cuadrática")

num_a = int(input("Ingrese 1º número: "))
num_b = int(input("Ingrese 2º número: "))
num_c = int(input("Ingrese 3º número: "))

root_1 = (-num_b + (num_b ** 2 - 4 * num_a * num_c) ** 0.5) / (2 * num_a)
root_2 = (-num_b - (num_b ** 2 - 4 * num_a * num_c) ** 0.5) / (2 * num_a)

print(f"1º fórmula cuadrática: {root_1}")
print(f"2º fórmula cuadrática: {root_2}")