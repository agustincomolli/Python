import socket
import time

host = "data.pr4e.org"
puerto = 80
navegador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
navegador.connect((host, puerto))
navegador.sendall(b"GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n")
contador = 0
imagen = b""

while True:
    datos = navegador.recv(5120)
    if len(datos) < 1: break
    time.sleep(0.25)
    contador += len(datos)
    print(f"Recibiendo: {len(datos)} bytes - Acumulado: {contador} bytes")
    imagen += datos

navegador.close()

# Buscar el encabezado (2CRLF)
posicion = imagen.find(b"\r\n\r\n")
print("\nLargo de la cabecera:", posicion, "\n")
print(imagen[:posicion].decode())

# Omitir el encabezado y guardar los datos de la imágen.
imagen = imagen[posicion + 4:]
archivo = open("imagen.jpg", mode="wb")
archivo.write(imagen)
archivo.close()