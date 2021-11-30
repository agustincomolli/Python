import unittest

from validacion import validar_usuario

class TestValidarUsuario(unittest.TestCase):
    def test_valido(self):
        self.assertEqual(validar_usuario("usuariovalido", 3), True)
    
    def test_muycorto(self):
        self.assertEqual(validar_usuario("inv", 5), False)

    def test_caracteres_invalidos(self):
        self.assertEqual(validar_usuario("usuario_invalido", 1), False)

    def test_minlen_invalido(self):
        self.assertRaises(ValueError, validar_usuario, "usuario", -1)

# Ejecutar prueba.
unittest.main()