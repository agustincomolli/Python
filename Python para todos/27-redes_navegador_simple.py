import socket

navegador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
navegador.connect(("data.pr4e.org", 80))
comando = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
navegador.send(comando)

while True:
    datos = navegador.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end="")

navegador.close()