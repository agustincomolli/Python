import datetime
import time
import locale


class Student:
    def take_nap(self, seconds):
        print("Estoy muy cansado. Tengo que hecharme una siesta. ", end="")
        print("¡Hasta luego!... 😴")
        time.sleep(seconds)
        print("Dormí bien. ¡Me siento genial! 🤩")


# Configura el programa en español de Argentina.
locale.setlocale(locale.LC_ALL, "es_AR")

my_birthday = datetime.date(1977, 6, 10)
year = my_birthday.year
month = my_birthday.strftime("%B")
day = my_birthday.day

print(f"Tú cumpleaños es el {day} de {month} de {year}\n")


student = Student()
student.take_nap(3)

print(f"\nHoy es {datetime.datetime.today().strftime('%d-%m-%Y')}")