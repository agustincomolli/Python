from formas import Paper, Rectangle, Triangle, Oval

lienzo = Paper()

obalo = Oval()
obalo.randomize()
obalo.draw()

triangulo = Triangle(100, 150, 200, 50, 300, 150)
triangulo.set_color("red")
triangulo.draw()

lienzo.display()