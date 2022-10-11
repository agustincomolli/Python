""" 
Cree un programa grades.py que verifique si una calificación está por encima o por debajo de 55.

Comience creando una variable llamada gradey asígnele un valor que esté entre 0 y 100.

Escriba una declaración if/ elsepara lo siguiente:

Si la calificación es mayor o igual a 55, escriba "Aprobó".
De lo contrario, escriba "Falló". 

"""

grade = int(input("Ingrese la calificación del alumno: "))

if grade >= 55:
    print("¡Aprobó! 😀")
else:
    print("¡Falló! 😢")