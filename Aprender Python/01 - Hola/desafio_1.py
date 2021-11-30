print("¿Cuál es la fecha de hoy?")
fecha = input()
print("Ingrese las calorías ingeridas en el desayuno: ")
calorias_desayuno = int(input())
print("Ingrese las calorías ingeridas en el almuerzo: ")
calorias_almuerzo = int(input())
print("Ingrese las calorías ingeridas en la merienda: ")
calorias_merienda = int(input())
print("Ingrese las calorías ingeridas en la cena: ")
calorias_cena = int(input())

calorias_totales = calorias_desayuno + calorias_almuerzo + calorias_merienda + calorias_cena
print("Total de calorías consumidas el " + fecha + ": " + str(calorias_totales))