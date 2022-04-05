class Encuesta_Anonima:
    """Recopile respuestas anónimas a una pregunta de encuesta."""

    def __init__(self, pregunta) -> None:
        """Guarde una pregunta y prepárese para almacenar respuestas."""
        self.pregunta = pregunta
        self.respuestas = []

    
    def mostrar_pregunta(self):
        """Mostrar la pregunta de la encuesta."""
        print(self.pregunta)


    def guardar_respuesta(self, nueva_respuesta):
        """Almacena una única respuesta a la encuesta."""
        self.respuestas.append(nueva_respuesta)


    def mostrar_resultados(self):
        """Mostrar todas las respuestas que se han dado."""
        print("Resultados de la encuesta:")
        for respuesta in self.respuestas:
            print(f"- {respuesta}")