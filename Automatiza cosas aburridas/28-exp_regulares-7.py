# Caracteres especiales.

from ast import expr
import re

exp_reg = re.compile(r"\d+\s\w+")
resultado = exp_reg.findall("12 tamborileros, 11 gaiteros, 10 señores, " + 
                            "9 damas, 8 doncellas, 7cisnes, 6 gansos, " + 
                            "5 anillos , 4 pájaros, 3 gallinas, 2 palomas, " + 
                            "1 perdiz")
print(resultado)

exp_reg = re.compile(r"[aeiouAEIOU]")
resultado = exp_reg.findall("Robocop come una comida para bebes")
print(resultado)

exp_reg = re.compile(r"[^aeiouAEIOU]")
resultado = exp_reg.findall("Robocop come una comida para bebes")
print(resultado)