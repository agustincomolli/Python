def es_bisiesto(año):
    return (año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0)

    # if año % 4 == 0:
    #     if año % 100 !=0 or año % 400 == 0:
    #         return True
    # else:
    #     return False


año = int(input("Ingrese un año para saber si es bisiesto o no: "))
print(f"{año} es bisiesto? {es_bisiesto(año)}")
