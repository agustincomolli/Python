import unittest
from modulo_encuesta import Encuesta_Anonima

class TestEncuestaAnonima(unittest.TestCase):
    """Prueba para la clase Encuesta_Anonima."""

    def setUp(self):
        """Cree una encuesta y un conjunto de respuestas para usar en todos 
        los métodos de prueba."""
        pregunta = "¿Qué idioma aprendiste a hablar primero?"
        self.mi_encuesta = Encuesta_Anonima(pregunta)
        self.respuestas = ["Español", "Inglés", "Italiano"]      


    def test_guardar_respuesta_simple(self):
        """Probar si una respuesta simple se guarda correctamente."""
        self.mi_encuesta.guardar_respuesta(self.respuestas[0])
        self.assertIn("Español", self.mi_encuesta.respuestas)


    def test_guardar_tres_respuestas(self):
        """Probar si tres respuestas se guardaron correctamente."""
        for respuesta in self.respuestas:
            self.mi_encuesta.guardar_respuesta(respuesta)
        
        for respuesta in self.respuestas:
            self.assertIn("Español",self. mi_encuesta.respuestas)


unittest.main()