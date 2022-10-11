""" 
Cree un programa ph_levels.py que compruebe si un nivel de pH es básico, ácido o neutro.

Primero, cree una variable llamada ph y solicite al usuario un valor entre 0 y 14.

Escriba un enunciado if, elif, elseque:

Si ph es mayor que 7, emite "Básico".
Si ph es menor que 7, emite "Ácido".
De lo contrario, salida "Neutral". 

"""

print("Nivel de pH 🧪\n")

ph = int(input("Ingrese un valor de pH (0-14): "))

if ph > 7:
    print("Básico")
elif ph < 7:
    print("Ácido")
else:
    print("Neutral")