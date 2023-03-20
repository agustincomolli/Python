import os
import shutil
from datetime import datetime, timedelta
from mylib import *


def get_week_month():
    """
    Description: Devuelve el número de la semana que corresponde a la fecha 
                 actual.
                 La fórmula calcula el día de la semana del primer día del mes 
                 y ajusta la cantidad de días a considerar para la primera 
                 semana del mes. En este caso, si el primer día del mes es un 
                 domingo, entonces se resta 1 a la cantidad de días 
                 considerados para la primera semana. Luego, se calcula el 
                 número de semanas completas que han pasado hasta la fecha 
                 actual y se le suma uno para obtener el número de la semana 
                 correspondiente al mes actual.
    """

    # Obtiene la fecha actual
    today = datetime.date.today()

    # Obtiene el año, mes y día de la fecha actual
    year, month, day = today.year, today.month, today.day

    # Obtiene la fecha del primer día del mes actual
    first_day_of_month = datetime.date(year, month, 1)

    # Obtiene el día de la semana del primer día del mes actual 
    # (0=lunes, 1=martes, ..., 6=domingo)
    first_day_of_month_weekday = first_day_of_month.weekday()

    # Si el primer día del mes es un domingo, ajusta la cantidad de días 
    # considerados para la primera semana del mes
    if first_day_of_month_weekday == 6:
        first_day_of_month_weekday = -1

    # Calcula el número de la semana del mes correspondiente a la fecha actual
    week_of_month = (day + first_day_of_month_weekday) // 7 + 1

    return week_of_month


def get_month_week_day():
    """
    Description: Obtiene el nombre del mes actual, el número de la semana
                 correspondiente al mes actual, y el nombre del día actual.
    Returns:     Devuelve una tupla con los tres valores correspondientes.
    """

    # Diccionario para convertir los nombres de los meses y días a español
    months_spanish = {
        'January': 'Enero',
        'February': 'Febrero',
        'March': 'Marzo',
        'April': 'Abril',
        'May': 'Mayo',
        'June': 'Junio',
        'July': 'Julio',
        'August': 'Agosto',
        'September': 'Septiembre',
        'October': 'Octubre',
        'November': 'Noviembre',
        'December': 'Diciembre'
    }

    days_spanish = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }

    # Obtenemos la fecha actual
    current_date = datetime.now()

    # Obtenemos el número de semana correspondiente al mes
    week_month = get_week_month()
    # Creamos los nombres de las carpetas según la fecha actual
    month = months_spanish[current_date.strftime('%B')]
    week = f'{week_month}° Sem'
    day = days_spanish[current_date.strftime('%A')]

    return month, week, day


def create_directories(destination: os.path):
    """
    Description: Crea los directorios donde se copiará el backup.
    """

    # Si la carpeta final no existe, la creamos
    if not os.path.exists(destination):
        os.makedirs(destination)


def copy_backup(source_path: str, destination_path: str):
    month, week, day = get_month_week_day()
    # Creamos la ruta de la carpeta final
    destination_path = os.path.join(destination_path, month, week, day)
    # Creamos los directorios.
    create_directories(destination_path)
    # Obtenemos la lista de archivos en la carpeta de origen
    files = os.listdir(source_path)

    # Obtenemos el primer archivo de la lista
    file_name = files[0]

    # Copiamos el archivo de backup a la carpeta final
    file_source_path = os.path.join(source_path, file_name)
    file_destination_path = os.path.join(destination_path, file_name)

    print(f"\nCopiando {file_source_path}...")
    try:
        shutil.copy(file_source_path, file_destination_path)
    except Exception as error:
        show_error(f"\nOcurrió un error al copiar el archivo 😭:\n{error}\n")
    else:
        print("\nArchivo copiado correctamente. ✔️\n")


def check_date():
    """
    Description: Comprueba si la fecha es menor al 10/01 del año actual y envía
                 un recordatorio al usuario para actualizar los parámetros del
                 backup en el servidor.
    """

    current_date = datetime.now()
    reminder_date = datetime(current_date.year, 1, 10)
    if current_date < reminder_date:
        message = "\n📆 RECORDATORIO: Agregar la carpeta de liquidaciones y "
        message += "del ejercicio nuevo\n"
        print(color_me(message, "magenta"))
        press_enter_to_continue()


clear_screen()
# Imprimir los títulos
print(color_me("*** Copia de Backups 💾 ***", "yellow"))
print(color_me(f"\nBackup de SIFIM:\n{'=' * 17}", "blue"))
# Recordar si cambia el ejercicio de SIFIM.
check_date()
copy_backup("//servidor/backups", "e:/Backups SIFIM")

print(color_me(f"Backup de RAFAM:\n{'=' * 17}", "blue"))
copy_backup("//SRV-RAFAM-01/RafamBackup", "e:/Backups RAFAM")

press_enter_to_continue()
