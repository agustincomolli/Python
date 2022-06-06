# Detectar fechas en formato dd/mm/yyyy en un texto.

import re

def detectar_fechas(texto):
    """Devuelve una lista de tuplas con las fechas encontradas."""
    texto = str(texto)
    exp_reg = r"(\d+)/(\d+)/(\d{4})"
    fecha = re.compile(exp_reg)
    return fecha.findall(texto)


def es_fecha_valida(dia, mes, año):
    """Devuelve True si es una fecha válida."""
    dia = int(dia)
    mes = int(mes)
    año = int(año)

    if año < 1000 or año > 2999 or mes > 12:
        return False

    if mes == 2:
        if es_año_bisiesto(año):
            return dia <= 29
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return dia <= 30
    else:
        return dia <= 31


def es_año_bisiesto(año):
    """Devuelve True si el año es bisiesto."""
    año = int(año)
    return (año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0)


fechas = detectar_fechas("29/02/1988, 10/6/1977, 01/01/0001, 11/09/1683, 29/02/1900, olé")
print(f"Se detectaron {len(fechas)} fechas en el texto.")
for indice, fecha in enumerate(fechas):
    dia, mes, año = fecha
    if es_fecha_valida(dia, mes, año):
        print(f"La {indice + 1}° fecha es válida: {dia}/{mes}/{año}")
    else:
        print(f"La {indice + 1}° fecha NO es válida: {dia}/{mes}/{año}")
