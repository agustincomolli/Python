import os

# Obtener datos de las variables de entorno en Linux.
print("HOME: ", os.environ.get("HOME", ""))
print("SHELL: ", os.environ.get("SHELL", ""))
print("FRUIT: ", os.environ.get("FRUIT", "variable no definida"))
# Si en el shell usamos el comando "export FRUIT=banana"...