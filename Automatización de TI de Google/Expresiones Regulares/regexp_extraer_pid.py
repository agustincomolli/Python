import re

# Extrae un grupo de números dentro de dos corchetes [].
def extraer_pid(linea_de_log):
    regexp = r"\[(\d+)\]"
    resultado = re.search(regexp, linea_de_log)
    if resultado is None:
        return ""
    return resultado[1]

# Ejemplo 1:
log = "July 31 07:51:48 mycompyter bad_process[12345]: ERROR Performing package upgrade"
print(extraer_pid(log))
# Ejemplo 2:
print(extraer_pid("99 elefantes en una [caja]"))

# Ejercicio:
# **********

# Agregue a la expresión regular utilizada en la función extract_pid, 
# para devolver el mensaje en mayúsculas entre paréntesis, 
# después de la identificación del proceso.

import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\b[A-Z]*\b)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
