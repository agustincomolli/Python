# 11-3. Empleado: Escribe una clase llamada Empleado. El método __init__() 
# debe tomar un nombre, un apellido y un salario anual, y almacenar cada uno 
# de estos como atributos. Escriba un método llamado give_raise() que 
# agregue $5000 al salario anual de manera predeterminada pero que también 
# acepte una cantidad de aumento diferente.
# Escriba un caso de prueba para Empleado. Escriba dos métodos de prueba, 
# test_give_ default_raise() y test_give_custom_raise(). Utilice el método 
# setUp() para no tener que crear una nueva instancia de empleado en cada 
# método de prueba. Ejecute su caso de prueba y asegúrese de que ambas 
# pruebas pasen.

class Empleado():
    """Guarda información sobre un empleado."""

    def __init__(self, nombre, apellido, salario_anual) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.salario_anual = salario_anual
    

    def dar_aumento(self, aumento_sueldo = 5000):
        """Aumentar el salario anual."""
        self.salario_anual += aumento_sueldo


import unittest

class TestEmpelado(unittest.TestCase):
    """Prueba de la clase empleado."""

    def setUp(self):
        """Crear un empleado para hacer todas las pruebas."""
        self.mi_empleado = Empleado("Agustín", "Comolli", 2730)

    def test_aumento_predeterminado(self):
        """Aumenta el sueldo anual de forma predeterminada."""
        self.mi_empleado.dar_aumento()
        self.assertEqual(7730, self.mi_empleado.salario_anual)

    def test_aumento_personalizado(self):
        """Aumenta el sueldo anual de forma personalizada."""
        self.mi_empleado.dar_aumento(9000)
        self.assertEqual(11730, self.mi_empleado.salario_anual)

unittest.main()