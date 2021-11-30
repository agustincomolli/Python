from arreglar_nombre import arreglar_nombre
import unittest

class TestArreglar(unittest.TestCase):
    def test_basico(self):
        caso_de_prueba = "Comolli, Agustín"
        esperado = "Agustín Comolli"
        self.assertEqual(arreglar_nombre(caso_de_prueba), esperado)

    def test_empty(self):
        caso_de_prueba = ""
        esperado = ""
        self.assertEqual(arreglar_nombre(caso_de_prueba), esperado)

    def test_dos_nombres(self):
        caso_de_prueba = "Comolli, Agustín A."
        esperado = "Agustín A. Comolli"
        self.assertEqual(arreglar_nombre(caso_de_prueba), esperado)

    def test_solo_nombre(self):
        caso_de_prueba = "Agustín"
        esperado = "Agustín"
        self.assertEqual(arreglar_nombre(caso_de_prueba), esperado)

unittest.main()