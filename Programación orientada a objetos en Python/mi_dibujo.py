from formas import Paper, Triangle, Rectangle, Oval

papel = Paper()

# Crear objeto.
rectangulo_1 = Rectangle()
# Establecer propiedades.
rectangulo_1.set_width(200)
rectangulo_1.set_height(100)
rectangulo_1.set_color("blue")
# Ejecutar método.
rectangulo_1.set_x(100)
rectangulo_1.set_y(100)
rectangulo_1.draw()

rectangulo_2 = Rectangle()
rectangulo_2.set_color("cyan")
rectangulo_2.set_height(150)
rectangulo_2.set_width(300)
rectangulo_2.set_x(150)
rectangulo_2.set_y(150)
rectangulo_2.draw()

papel.display()
