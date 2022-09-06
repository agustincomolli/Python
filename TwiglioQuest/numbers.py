import sys

# Este código lee argumentos y convierte esas entradas a números decimales.
first_number = float(sys.argv[1])
second_number = float(sys.argv[2])

result_sum = first_number + second_number
print(f"{first_number} + {second_number} = {result_sum}")

result_difference = first_number - second_number
print(f"{first_number} - {second_number} = {result_difference}")

result_product = first_number * second_number
print(f"{first_number} * {second_number} = {result_product}")

result_quotient = first_number / second_number
print(f"{first_number} / {second_number} = {result_quotient}")
