from mylib import clear_screen, color_me, input_color
import datetime

clear_screen()
print(color_me("⏰ Temporizador de eventos ⏰\n", "yellow"))
today = datetime.date.today()
event = input_color("Evento: ", color_input="green")
try:
    year = int(input_color("Año: ", color_input="green"))
    month = int(input_color("Mes: ", color_input="green"))
    day = int(input_color("Día: ", color_input="green"))
except:
    print(color_me("\nERROR: Debe ingresar un número entero.", "red"))
    exit()

date = datetime.date(year, month, day)
difference = (today - date).days

if difference == 0:
    print(color_me("\n¡HOY ES EL EVENTO! 🥳", "blue"))
elif difference > 0:
    print(color_me(f"\nHan pasado {difference.days} días del evento 😢", "magenta"))
elif difference < 0:
    print(color_me(f"\nFaltan {difference.days * -1} días para el evento 🙂"))
