class Animal:
    pasos = 0
    nombre = ""

    def __init__(self, nombre_animal) -> None:
        self.nombre = nombre_animal
        print(self.nombre, "construido")

    def caminar(self):
        self.pasos += 1
        if self.pasos == 1:
            print(f"{self.nombre} ha dado {self.pasos} paso.")
        else:
            print(f"{self.nombre} ha dado {self.pasos} pasos.")