import socket

navegador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pagina_web = input("Ingrese la URL: ")

try:
    # Dividir la URL para obtener sólo el dominio. Ej: www.google.com
    host = pagina_web.split("/")
    if len(host) > 2:
        host = host[2]
    else:
        host = host[0]
    navegador.connect((host, 80))
except:
    print("La URL ingresada no es válida o no está disponible.")
    quit()

comando = f"GET {pagina_web} HTTP/1.0\r\n\r\n".encode()
navegador.send(comando)
total_recibido = 0
documento = b""

# Descargar la página a la memoria y contar el total de
# caracteres recibidos.
while True:
    datos = navegador.recv(512)
    if len(datos) < 1:
        break
    total_recibido += len(datos.decode())
    documento += datos

navegador.close()

# Buscar el encabezado y a partir de ahí mostrar la página.
posicion = documento.find(b"\r\n\r\n")
documento = documento[posicion + 4:].decode().splitlines()
total = 0
for linea in documento:
    total += len(linea)
    if total <= 3000:
        print(linea)
print("\nTotal de caracteres recibidos:", total_recibido)
