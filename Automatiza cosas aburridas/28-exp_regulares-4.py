import re

# Coincidencia de 0 o más caracteres.
print("Coincidencia de 0 o más caracteres.")
exp_reg = re.compile(r"Bat(wo)*man")
resultado = exp_reg.search("Las aventuras de Batman.")
print(resultado.group())
resultado = exp_reg.search("Las aventuras de Batwoman.")
print(resultado.group())
resultado = exp_reg.search("Las aventuras de Batwowowowoman.")
print(resultado.group())

# Coincidencia de 1 o más caracteres.
print("\nCoincidencia de 1 o más caracteres.")
exp_reg = re.compile(r"Bat(wo)+man")
resultado = exp_reg.search("Las aventuras de Batman.")
if resultado == None:
    print("No hay coincidencias en esta frase.")
resultado = exp_reg.search("Las aventuras de Batwoman.")
print(resultado.group())
resultado = exp_reg.search("Las aventuras de Batwowowowoman.")
print(resultado.group())