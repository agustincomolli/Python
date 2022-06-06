import re

# Coincidencias codiciosas y no  codiciosas.

exp_reg = re.compile(r"(Ha){3,5}")
resultado = exp_reg.search("HaHaHaHaHa")
print("Búsqueda codiciosa:")
print(resultado.group())

exp_reg = re.compile(r"(Ha){3,5}?")
resultado = exp_reg.search("HaHaHaHaHa")
print("Búsqueda NO codiciosa:")
print(resultado.group())
