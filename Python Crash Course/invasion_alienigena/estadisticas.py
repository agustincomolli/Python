class Estadistica_Juego():
    """Seguir las estadísticas del juego."""

    def __init__(self, config_juego):
        """Inicializar las estadísticas."""

        self.config_juego = config_juego
        # Empezar el juego en estado inactivo.
        self.estado_juego = False
        self.reiniciar_estadisticas()


    def reiniciar_estadisticas(self):
        """Inicializar las estadísticas que pueden cambiar durante el juego."""
        self.naves_restantes = self.config_juego.limite_naves
        self.puntaje = 0
        self.nivel = 1
