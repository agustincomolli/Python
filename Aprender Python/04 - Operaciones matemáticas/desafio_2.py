print("\n","¡Calculadora simple!".center(40), "\n", ("*" * 20).center(40), "\n")

primer_numero = input("Primer número: ")
if not primer_numero.isnumeric():
    print("Por favor ingrese un número.")
    exit()

operacion = input("Operación: ")

segundo_numero = input("Segundo número: ")
if not segundo_numero.isnumeric():
    print("Por favor ingrese un número.")
    exit()

print("")

if operacion == "+":
    resultado = int(primer_numero) + int(segundo_numero)
    etiqueta = "Suma"
elif operacion == "-":
    resultado = int(primer_numero) - int(segundo_numero)
    etiqueta = "Resta"
elif operacion == "*":
    resultado = int(primer_numero) * int(segundo_numero)
    etiqueta = "Multiplicación"
elif operacion == "/":
    resultado = int(primer_numero) / int(segundo_numero)
    etiqueta = "División"
elif operacion == "**":
    resultado = int(primer_numero) ** int(segundo_numero)
    etiqueta = "Potencia"
elif operacion == "%":
    resultado = int(primer_numero) % int(segundo_numero)
    etiqueta = "Módulo"
else:
    print("Operación no reconocida.")

print(f"{etiqueta} de {primer_numero} {operacion} {segundo_numero} = {resultado}")