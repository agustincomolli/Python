"""
Cree un programa currency.py que le pregunte al usuario la cantidad que 
tiene en yuanes, yenes y wones y calcule el total en USD.
"""

print("Cambio de divisas 💵\n")

yuan = int(input("¿Cuántos yuanes (chinos) tiene? "))
yen = int(input("¿Cuántos yenes (japoneses) tiene? "))
won = int(input("¿Cuántos wones (coreanos) tiene? "))

# Valor dólar hoy 08/10/2022
yuan_value = 0.14
yen_value = 0.0069
won_value = 0.00070

dollars_yuan = yuan * yuan_value
dollars_yen = yen * yen_value
dollars_won = won * won_value

print(f"\nTienes u$s {dollars_yuan + dollars_yen + dollars_won}")