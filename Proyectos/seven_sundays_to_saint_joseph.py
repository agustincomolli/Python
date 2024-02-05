from datetime import datetime, timedelta
import locale

def get_first_sunday_after(date):
    """
    Calcula la fecha del primer domingo después de una fecha específica.

    Args:
        fecha (datetime): La fecha de referencia.

    Returns:
        datetime: La fecha del primer domingo después de la fecha de referencia.
    """
    while date.weekday() != 6:  # 6 es el índice del domingo
        date += timedelta(days=1)
    return date

def format_date_to_local(date):
    """
    Convierte una fecha en formato local (es_AR) a una cadena legible.

    Args:
        fecha (datetime): La fecha a formatear.

    Returns:
        str: La fecha formateada en formato local.
    """
    # Establece el formato local para la fecha
    locale.setlocale(locale.LC_TIME, 'es_AR.utf8')
    formatted_date = date.strftime("%A %d %B de %Y")
    return formatted_date

def main():
    """
    Calcula y muestra la fecha del primer domingo de los Siete Domingos de San José.
    """
    # Obtener la fecha actual
    today  = datetime.today()

    # Calcular la fecha del 19 de marzo del año actual
    saint_joseph_date = datetime(today .year, 3, 19)

    # Restar 7 días a la fecha de San José para obtener la fecha de inicio "corregida"
    corrected_start_date = saint_joseph_date - timedelta(days=7 * 7)

    # Calcular el primer domingo después de la fecha de inicio corregida (debe ser 7/02/2024)
    first_sunday_celebration = get_first_sunday_after(corrected_start_date)

    # Convertir la fecha a formato local
    local_date = format_date_to_local(first_sunday_celebration)

    # Imprimir la fecha del primer domingo de la celebración
    print(f"El primer domingo de los 7 domingos de San José debe ser el: {local_date}")

if __name__ == "__main__":
    main()
