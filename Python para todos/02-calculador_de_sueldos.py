# Calcular el sueldo de un empleado. Si trabajó más de 40 horas
# darle 50 % más.
def calcular_sueldo(horas, tarifa):
    if horas > 40:
        sueldo_regular = 40 * tarifa
        sueldo_extra = (horas - 40) * (tarifa * 1.5)
        sueldo = sueldo_regular + sueldo_extra
    else:
        sueldo = horas * tarifa
    return sueldo

    
print("Calculadora de sueldos\n" + "=" * 22)
try:
    horas = float(input("\nHoras trabajadas: "))
    tarifa = float(input("Tarifa por hora: "))
except:
    print("Debe ingresar un valor numérico.")
    quit()

print("\nDeberá pagar $ " + str(calcular_sueldo(horas, tarifa)) + " \n")
