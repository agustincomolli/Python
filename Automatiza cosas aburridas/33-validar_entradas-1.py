import pyinputplus as pyip

# Validar entradas numericas.
print(pyip.inputNum("Ingrese un número: ",))
print(pyip.inputNum("Ingrese un número '>= 4': ", min=4))
print(pyip.inputNum("Ingrese un número '> 4': ", greaterThan=4))
print(pyip.inputNum("Ingrese un número '>= 4 y < 6': ", min=4, lessThan=6))

# Permitir entradas vacias.
print(pyip.inputNum("Ingrese un número (puede ingresar nada): ", blank=True))

# Validar entradas numericas con limites de intentos.
try:
    print(pyip.inputNum("Ingrese un número (intentos = 2): ", limit=2))
except pyip.RetryLimitException:
    print("Intentos excedidos.")

# Validar entradas numéricas con tiempo de espera.
try:
    print(pyip.inputNum("Ingrese un número (espera = 5): ", timeout=5))
except pyip.TimeoutException:
    print("Tiempo de espera excedido.")

# Validar entradas numéricas con expresiones regulares.
print(pyip.inputNum("Ingrese un número (números romanos): ", 
                    allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"]))

print(pyip.inputNum("Ingrese un número que no sea par: ", 
                    blockRegexes=[r"[2468]$"]))
