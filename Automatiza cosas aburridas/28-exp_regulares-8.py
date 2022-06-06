# Coincidir al principio y al final de la cadena.

import re

comienza_con = re.compile(r"^Hola")
resultado = comienza_con.search("Hola, buen día")
print(resultado)

comienza_con = re.compile(r"^Hola")
resultado = comienza_con.search("Él no dijo hola")
print(resultado)

termina_con = re.compile(r"\d+$")
resultado = termina_con.search("Tú DNI es 26047917")
print(resultado)