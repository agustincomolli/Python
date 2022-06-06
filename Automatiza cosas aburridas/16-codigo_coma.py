def transformar_lista(lista):
    """Transforma una lista en una cadena con sus valores 
    separados por comas."""

    if len(lista) == 0: return ""

    resultado = ""
    for item in lista[:-1]:
        resultado += str(item) + ", "
    resultado += "y " + lista[-1]
    
    return resultado

lista_ejemplo = ["peras", "bananas", 123, True, "perros", "gatos"]
print(transformar_lista(lista_ejemplo))
