def chequear_numero_primo(numero):
    for factor in range(2, numero -1):
        if numero % factor == 0:
            return (False, factor)
            break
    return (True, 0)

numeros_a_chequear = [26, 39, 51, 53, 57, 79, 85]

for numero in numeros_a_chequear:
    es_primo, factor = chequear_numero_primo(numero)
    if not es_primo:
        print(f"{numero} NO ES un número primo, porque {factor} es factor de {numero}")
    else:
        print(f"{numero} ES un número primo.")
