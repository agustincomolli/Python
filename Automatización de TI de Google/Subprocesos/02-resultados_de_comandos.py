import subprocess

# Ejecutar el comando host
resultado = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# Imprimir el resultado de la operación: 0 = operación exitosa
print(resultado.returncode)
# Imprimir la salida generada por el comando.
print(resultado.stdout)
# Decodificar y dividir los datos de la salida.
print(resultado.stdout.decode())

# Eliminar un archivo que no existe.
resultado = subprocess.run(["rm", "el_archivo_no_existe.txt"], capture_output=True)
# Imprimir la salida generada por el comando.
print(resultado.returncode)
# Imprimir la salida generada por el comando.
print(resultado.stdout)
# Imprimir la salida de error.
print(resultado.stderr.decode())
