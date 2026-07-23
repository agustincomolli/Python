from mylib import clear_screen, color_me
import csv


with open("./Day54Totals.csv", mode="r", encoding="UTF-8") as file:
    reader = csv.DictReader(file)
    total = 0

    for row in reader:
        total += float(row["Cost"]) * int(row["Quantity"])

clear_screen()
print(color_me("🪙 REGISTRO DE VENTAS 🪙\n" + "=" * 23, "yellow"))
print(f"\nHoy su tienda vendió por $ {round(total, 2)}")
