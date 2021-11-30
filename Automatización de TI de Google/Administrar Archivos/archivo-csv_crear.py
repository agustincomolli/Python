import csv, os

hosts = [["Servidor SIFIM","192.168.2.5"],["Servidor RAFAM", "192.168.2.3"],["Servidor Web", "192.168.2.7"]]

if os.path.exists("hosts.csv"):
    os.remove("hosts.csv")

with open("hosts.csv", "w") as archivo:
    archivo_csv = csv.writer(archivo)
    # Escribir todo el contenido de la lista en el archivo.
    archivo_csv.writerows(hosts)
