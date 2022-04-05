# 11-1. Ciudad, País: Escriba una función que acepte dos parámetros: un 
# nombre de ciudad y un nombre de país. La función debe devolver una única 
# cadena con el formato Ciudad, País, como Santiago, Chile. Almacene la 
# función en un módulo llamado city_functions.py.
# Cree un archivo llamado test_cities.py que pruebe la función que acaba de 
# escribir (recuerde que necesita importar unittest y la función que desea 
# probar). Escriba un método llamado test_city_country() para verificar que 
# llamar a su función con valores como 'santiago' y 'chile' da como resultado 
# la cadena correcta. Ejecute test_cities.py y asegúrese de que 
# test_city_country() pase.

# 11-2. Población: modifique su función para que requiera un tercer parámetro, 
# la población. Ahora debería devolver una sola cadena con el formato Ciudad, 
# País – población xxx, como Santiago, Chile – población 5000000. Ejecute 
# test_cities.py nuevamente. Asegúrate de que test_city_country() falle 
# esta vez.
# Modifique la función para que el parámetro de población sea opcional. 
# Vuelva a ejecutar test_cities.py y asegúrese de que test_city_country() 
# vuelva a pasar.
# Escriba una segunda prueba llamada test_city_country_population() que 
# verifique que puede llamar a su función con los valores 'santiago', 'chile' 
# y 'population=5000000'. Vuelva a ejecutar test_cities.py y asegúrese de 
# que pase esta nueva prueba.

import unittest

def obtener_ciudad_pais(ciudad, pais, poblacion=None):
    """Devuelve una cadena formateada con la ciudad y su país 
    correspondiente."""
    
    if poblacion:
        ciudad_pais = f"{ciudad.title()}, {pais.title()} - población: " + \
            f"{poblacion}."
    else:
        ciudad_pais = f"{ciudad}, {pais}".title()

    return ciudad_pais


class Prueba_Ciudad_Pais(unittest.TestCase):
    """Prueba para la función obtener_ciudad_pais()."""
    
    def test_ciudad_pais(self):
        """Chequear que los valores Buenos Aires, Argentina sean correctos."""
        ubicacion = obtener_ciudad_pais("buenos aires", "argentina")
        self.assertEqual(ubicacion, "Buenos Aires, Argentina")
    

    def test_ciudad_pais_poblacion(self):
        ubicacion = obtener_ciudad_pais("cañuelas", "argentina", "65000")
        self.assertEqual(ubicacion, "Cañuelas, Argentina - población: 65000.")

unittest.main()