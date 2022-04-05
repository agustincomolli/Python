import unittest
from modulo_nombres import obtener_nombre_formateado

class Nombre_Prueba(unittest.TestCase):
    """Prueba para modulo_nombres.py"""

    def test_nombre_formateado(self):
        """Chequear si hacer nombres como Agustín Comolli funciona."""
        nombre_formateado = obtener_nombre_formateado("agustín", "comolli")
        self.assertEqual(nombre_formateado, "Agustín Comolli")


    def test_nombre_completo(self):
        """Chequear si los nombres que tienen dos nombres como Agustín
            Alfredo Comolli funcionan."""
        nombre_formateado = obtener_nombre_formateado("wolfgang", \
            "mozart", "amadeus")
        self.assertEqual(nombre_formateado, "Wolfgang Amadeus Mozart")

while True:
    nombre = input("Ingrese el nombre [s = salir]: ")
    if nombre.lower() == "s":
        break
    
    segundo_nombre = input("Ingrese el segundo nombre [s = salir]: ")
    if segundo_nombre.lower() == "s":
        break

    apellido = input("Ingrese el apellido [s = salir]: ")
    if apellido.lower() == "s":
        break

    nombre_completo = obtener_nombre_formateado(nombre, apellido, segundo_nombre)
    print(f"\nNombre completo: {nombre_completo}")

unittest.main()