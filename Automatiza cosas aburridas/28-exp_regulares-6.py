# Método findall()

import re

# Sin grupos.
exp_reg = re.compile(r"\d{3}-\d{3}-\d{4}")
resultado = exp_reg.findall("Celular: 415-555-9999 Trabajo: 212-555-0000")
print(resultado)

# Con grupos.
exp_reg = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
resultado = exp_reg.findall("Celular: 415-555-9999 Trabajo: 212-555-0000")
print(resultado)