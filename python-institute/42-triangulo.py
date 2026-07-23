"""
Además, vamos a poner tres puntos en una clase, lo que nos permitirá definir 
un triángulo.¿Cómo podemos hacerlo?

La nueva clase se llamará Triangle y esto es lo que queremos:

- El constructor acepta tres argumentos - todos ellos son objetos de la clase 
Point.
- Los puntos se almacenan dentro del objeto como una lista privada
- La clase proporciona un método sin parámetros llamado perimeter(), que 
calcula el perímetro del triángulo descrito por los tres puntos; el perímetro 
es la suma de todas las longitudes de los lados (lo mencionamos para que 
conste, aunque estamos seguros de que tú mismo lo conoces perfectamente).

"""

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:

    __vertices = []

    def __init__(self, vertice1:Point, vertice2:Point, vertice3:Point):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        total = 0
        for i in range(3):
            if i < 2:
                total += self.__vertices[i].distance_from_point(self.__vertices[i + 1])
            else:
                total += self.__vertices[i].distance_from_point(self.__vertices[0])
        return total


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
