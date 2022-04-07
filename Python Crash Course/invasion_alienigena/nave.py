import pygame
from pygame.sprite import Sprite

class Nave(Sprite):

    def __init__(self, config_juego, pantalla) -> None:
        """Inicializa la nave y establece su posición inicial."""

        super(Nave,self).__init__()

        self.config_juego = config_juego
        self.pantalla = pantalla
        # Cargar la imagen de la nave y obtener su rectángulo.
        self.image = pygame.image.load("imagenes/nave.png")
        self.rect = self.image.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        # Empezar cada nave en el centro-abajo de la pantalla.
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom - self.rect.height

        # Almacenar un valor decimal para el centro de la nave.
        self.centro = float(self.rect.centerx)

        # Bandera de movimiento.
        self.moviendo_derecha = False
        self.moviendo_izquierda = False


    def actualizar(self):
        """Actualiza la posición de la nave en base a la bandera de 
        movimiento"""
        if self.moviendo_derecha and \
            self.rect.right < self.pantalla_rect.right:
            # Mover a la derecha si no llega al borde.
            self.centro += self.config_juego.factor_velocidad
        elif self.moviendo_izquierda and self.rect.left > 0:
            # Mover a la izquierda si no llega al borde.
            self.centro -= self.config_juego.factor_velocidad
        
        self.rect.centerx = self.centro


    def dibujame(self):
        """Dibuja la nave en la ubicación actual."""
        self.pantalla.blit(self.image, self.rect)

    
    def centrar_nave(self):
        """Centrar la nave en la pantalla."""
        self.centro = self.pantalla_rect.centerx