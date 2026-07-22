class Alumno:

    def __init__(self, nombre, apellido, nota, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota
        self.dni = dni


    def mostrar_estado(self):
        if self.nota >= 4:
            print("El alumno", self.nombre, "esta aprobado")
        else:
            print("El alumno", self.nombre, "esta desaprobado")



#Programa principal

alumno1 = Alumno("Juan", "Perez", 8, 12345678)
alumno2 = Alumno("Maria", "Gomez", 3, 23456789)


print(alumno1.nombre)
print(alumno1.apellido)
print(alumno1.nota)

print(alumno2.nombre)
print(alumno2.apellido)
print(alumno2.nota)

alumno1.mostrar_estado()
alumno2.mostrar_estado()