import shelve

ruta_archivo = "./Automatiza cosas aburridas/configuraciones"

# Guardar variables en un archivo binario.
configuraciones = shelve.open(ruta_archivo)
colores = ["rojo", "verde", "azul"]
configuraciones["colores"] = colores
configuraciones.close()

# Recuperar datos almacenados.
configuraciones = shelve.open(ruta_archivo)
print(configuraciones["colores"])
configuraciones.close()