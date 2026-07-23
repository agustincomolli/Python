# Crear un función que devuelva el número máximo de una lista.

def obtener_mayor(lista):
    mayor = 0

    for i in lista:
        if i > mayor:
            mayor = i

    return mayor

numeros = [1, 100, 80, 125, 44, 119, 200, 24, 199]

print(f"El número mayor es: {obtener_mayor(numeros)}")