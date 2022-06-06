import re

# Coincidencia opcional.
exp_reg = re.compile(r"Bat(wo)?man")
resultado = exp_reg.search("Las aventuras de Batman.")
print(resultado.group())
resultado = exp_reg.search("Las aventuras de Batwoman.")
print(resultado.group())