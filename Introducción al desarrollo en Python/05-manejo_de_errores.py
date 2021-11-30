x = 42
y = 0

print("Errores:\n" + "=" * 8)
print(f"{x} / {y}")
try:
    print(x / y)
except ZeroDivisionError as error:
    print("ERROR: No se puede dividir un número por cero.")
else:
    print("ERROR. Algo ha ocurrido con su programa.")
finally:
    print("Código limpio")