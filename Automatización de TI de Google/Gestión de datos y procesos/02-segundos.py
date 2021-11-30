#!/usr/bin/env python3

def a_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

print("\n¡Bienvenido a este convertidor de tiempo!")

continuar = "s"

while continuar.lower() == "s":
    horas = int(input("\nIngrese el número de horas: "))
    minutos = int(input("Ingrese el número de minutos: "))
    segundos = int(input("Ingrese el número de segundos: "))
    
    print("\nSon {} segundos\n".format(a_segundos(horas, minutos, segundos)))

    continuar = input("¿Desea hacer otra conversión? [s para continuar]: ")

print("\n¡Adiós!")