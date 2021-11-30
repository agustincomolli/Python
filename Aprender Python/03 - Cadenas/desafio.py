primer_valor = "  PRIMER desafío         "
segundo_valor = "-  segundo desafío  -"
tercer_valor = "tE RCE R-D ESA FIO"
cuarto_valor = "cuarto"
quinto_valor = "quinto"
sexto_valor = "sexto"

primer_valor = primer_valor.title().strip().center(30)
segundo_valor = segundo_valor.strip(" - ").capitalize()
tercer_valor = tercer_valor.replace(" ", "").replace("-", " ").capitalize().rjust(30)

print(primer_valor)
print(segundo_valor)
print(tercer_valor)

print(cuarto_valor, quinto_valor, sexto_valor, sep="#", end="!")
print(f"\t{cuarto_valor}\n\t{quinto_valor}\n\t{sexto_valor}")