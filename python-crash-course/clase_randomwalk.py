from random import choice
from weakref import proxy

class RandomWalk():
    """Una clase que genera caminos aleatorios."""

    def __init__(self, num_puntos=5000):
        """Inicializar los atributos del camino."""

        self.num_puntos = num_puntos
        # Todos los caminos empiezan en (0, 0).
        self.valores_x = [0]
        self.valores_y = [0]


    def llenar_camino(self):
        """Calcular todos los puntos en el camino."""

        # Siga dando pasos hasta que la caminata alcance la longitud deseada.
        while len(self.valores_x) < self.num_puntos:
            # Decidir en qué dirección ir y qué tan lejos ir en esa dirección.
            direccion_x = choice([1, -1])
            distancia_x = choice([0, 1, 2, 3, 4])
            paso_x = direccion_x * distancia_x

            direccion_y = choice([1, -1])
            distancia_y = choice([0, 1, 2, 3, 4])
            paso_y = direccion_y * distancia_y

            # Rechaza movimientos que no van a ninguna parte.
            if paso_x == 0 and paso_y == 0:
                continue

            # Calcular el próximo valor x e y.
            proximo_x = self.valores_x[-1] + paso_x
            proximo_y = self.valores_y[-1] + paso_y

            self.valores_x.append(proximo_x)
            self.valores_y.append(proximo_y)