# Crear una función que acepte una lista arbitraria de argumentos
print("\nPaso 1: \n********")

def print_args(*argumentos):
    for argumento in argumentos:
        print(f"Argumento: {argumento}")
    print(f"Los argumentos son de clase: {type(argumentos)}")

print_args("a")
print_args("a", "b")
print_args("a", "b", "c")

# Aceptar argumentos de palabra clave
print("\nPaso 2: \n********")

def print_keyword_args(**kwargs):
    tercero =   kwargs.get("tercero", None)
    if tercero != None:
        print("El tercer argumento es: ", tercero)

print_keyword_args(primer="a")
print_keyword_args(primer="b", segundo="c")
print_keyword_args(primer="d", segundo="e", tercero="f")

# Iterar en cada palabra clave y valor
print("\nPaso 3: \n********")

def print_keyword_args(**kwargs):
    
    print("\n")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

    tercero = kwargs.get("tercero", None)
    if tercero != None:
        print("El tercer argumento es: ", tercero)

print_keyword_args(primero="a")
print_keyword_args(primero="b", segundo="c")
print_keyword_args(primero="d", segundo="e", tercero="f")

# Imprimir el valor de kwargs y su tipo de datos
print("\nPaso 4: \n********")

def print_keyword_args(**kwargs):
    
    print("\n")
    print(kwargs)
    print(type(kwargs))

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

    tercero = kwargs.get("tercero", None)
    if tercero != None:
        print("El tercer argumento es: ", tercero)

print_keyword_args(primero="a")
print_keyword_args(primero="b", segundo="c")
print_keyword_args(primero="d", segundo="e", tercero="f")