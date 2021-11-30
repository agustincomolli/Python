from obj_clase_animal import Animal

class Perro(Animal):
    raza = ""

    def __init__(self, nombre_animal, raza_perro) -> None:
        super().__init__(nombre_animal)
        self.raza = raza_perro

    def ladrar(self):
        print("¡Guau, guau, guau!")

Mendieta = Perro("Mendieta", "Border Collie")
Mendieta.ladrar()