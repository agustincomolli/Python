import re

resultado = re.search(r"aza", "plaza")
print(resultado)
resultado = re.search(r"aza", "bazaar")
print(resultado)
print("\"bazaar\"[1:4] = ", "bazaar"[1:4])
# Si el resultado no existe...
resultado = re.search(r"aza", "otra cosa")
# ... devuelve none.
print(resultado)
# El símbolo ^ seguido del caracter busca ese caracter al principio de la línea.
print(re.search(r"^x", "xenon"))
# El . reemplaza a cualquier caracter.
print(re.search(r"p.ng", "pingüino"))
print(re.search(r"p.ng", "exponga"))

def chequear_aei(texto):
    resultado = re.search(r"a.e.i", texto)
    return resultado != None

print(chequear_aei("academia"))
print(chequear_aei("aerio"))
print(chequear_aei("paramedico"))