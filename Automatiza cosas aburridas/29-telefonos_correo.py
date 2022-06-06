# Buscar teléfonos y direcciones de email dentro del contenido del 
# portapapeles.

import pyperclip
import re

telefono_exp_reg = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                  # Código de área.
    (\s|-|\.)?                          # Separador.
    (\d{3})                             # Primeros 3 dígitos.
    (\s|-|\.)                           # Separador.
    (\d{4})                             # Últimos 4 dígitos.
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # Extensión.
    )""", re.VERBOSE)

email_exp_reg = re.compile(r"""(
    [a-zA-Z0-9._%+-]+   # Nombre de usuario.
    @                   # Símbolo @.
    [a-zA-z0-9.-]+      # Dominio.
    (\.[a-zA-Z]{2,4})   # . algo.
    )""", re.VERBOSE)

# Pegar el contenido del portapapeles y convertirlo a texto.
texto = str(pyperclip.paste())
# Encontrar las coincidencias de números de teléfono e email.
coincidencias = []
for grupos in telefono_exp_reg.findall(texto):
    telefono = "-".join([grupos[1], grupos[3], grupos[5]])
    if grupos[8] != "":
        telefono += " x" + grupos[8]
    coincidencias.append(telefono)
for grupos in email_exp_reg.findall(texto):
    coincidencias.append(grupos[0])

# Copiar las coincidencias al portapapeles.
if len(coincidencias) > 0:
    pyperclip.copy("\n".join(coincidencias))
    print("Copiado al portapapeles.")
    print("\n".join(coincidencias))
else:
    print("No hay teléfono números o direcciones de correo electrónico " +
          "encontrados.")