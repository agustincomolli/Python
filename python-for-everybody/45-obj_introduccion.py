class Animal:
    pasos = 0
    nombre = ""

    def __init__(self, nombre_animal) -> None:
        self.nombre = nombre_animal
        print(self.nombre, "construido")

    def caminar(self):
        self.pasos += 1
        if self.pasos == 1:
            print(f"He dado {self.pasos} paso.")
        else:
            print(f"He dado {self.pasos} pasos.")

    # Es muy raro usar el método destructor.
    def __del__(self):
        print(self.nombre,"ha dado", self.pasos, "pasos y ha sido destruido.")

mi_animal = Animal("Mendieta")
mi_animal.caminar()
mi_animal.caminar()
mi_animal.caminar()
mi_animal = 42
print("mi_animal contiene", mi_animal)