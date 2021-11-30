# Validar la entrada del usuario para permitir solamente
# números enteros entre 1900 y 2021.
def ingresar_año():
    año = input("Ingrese el año: ")
    es_valido = False

    while not es_valido:
        try:
            año = int(año)
            if año < 1900 or año > 2021:
                print("¡Dato no válido! Debe ingresar un número entero entre 1900 y 2021\n")
                raise ValueError()
            es_valido = True
        except ValueError as error:
            año = input("¡Dato no válido! Ingrese el año: ")
    
    return año

# Validar si un año es bisiesto.
def es_bisiesto(año):
    return (año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0)

# Validar entrada de usuario para que ingrese solamente el nombre del mes.
def ingresar_mes():
    meses_del_año = ["enero", "febrero","marzo",
                    "abril", "mayo", "junio",
                    "julio", "agosto", "septiembre",
                    "octubre", "noviembre", "diciembre"]
    
    mes = input("Ingrese el mes: ").lower()
    es_valido = False

    while not es_valido:
        if mes not in meses_del_año:
            print("¡Dato no válido! Ingrese el nombre del mes.")
            mes = input("Ingrese el mes: ").lower()
        else:
            es_valido = True

    return mes

# Validar entrada de usuario para aceptar números enteros
# entre 1 y 31 según sean los días del mes elegido anteriormente.
def ingresar_dia(mes, año):
    meses_dias = {
                    "enero" : 31, "febrero" : 28, "marzo" : 31,
                    "abril" : 30, "mayo" : 31, "junio" : 30,
                    "julio" : 31, "agosto" : 31, "septiembre" : 30,
                    "octubre" : 31, "noviembre" : 30, "diciembre" : 31
                }
    
    if es_bisiesto(año):
        meses_dias["febrero"] = 29

    dia = input("Ingrese el día: ")
    es_valido = False

    while not es_valido:
        try:
            dia = int(dia)
            if (dia < 1) or (dia > meses_dias[mes]):
                raise ValueError()
            es_valido = True
        except ValueError:
            print(f"¡Dato no válido! Ingrese un número entre 1 y {meses_dias[mes]}")
            dia = input("Ingrese el día: ")

    return dia

print("*** VALIDADOR DE FECHAS ***\n")
año = ingresar_año()
mes = ingresar_mes()
dia = ingresar_dia(mes, año)

print(f"Tu fecha es: {dia} de {mes} de {año}")