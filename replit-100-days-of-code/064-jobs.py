from mylib import color_me, clear_screen, press_enter_to_continue


class Job:

    name = None
    salary = None
    hours_worked = None

    def __init__(self, name, salary, hours_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked

    def print_info(self):
        print("*** TRABAJO ***\n")
        print(f"Nombre: {self.name}")
        print(f"Sueldo: ${self.salary}")
        print(f"Horas trabajadas: {self.hours_worked}")


class Doctor(Job):

    speciality = None
    years_experience = None

    def __init__(self, salary, hours_worked, speciality,
                 years_experience):
        self.name = "Doctor"
        self.salary = salary
        self.hours_worked = hours_worked
        self.speciality = speciality
        self.years_experience = years_experience

    def print_info(self):
        print("*** TRABAJO ***\n")
        print(f"Nombre: {self.name}")
        print(f"Especialidad: {self.speciality}")
        print(f"Experiencia: {self.years_experience} años")
        print(f"Sueldo: ${self.salary}")
        print(f"Horas trabajadas: {self.hours_worked}")


class Teacher(Job):

    subject = None
    position = None

    def __init__(self, salary, hours_worked, subject, position):
        self.name = "Profesor"
        self.salary = salary
        self.hours_worked = hours_worked
        self.subject = subject
        self.position = position

    def print_info(self):
        print("*** TRABAJO ***\n")
        print(f"Nombre: {self.name}")
        print(f"Asignatura: {self.subject}")
        print(f"Posición: {self.position}")
        print(f"Sueldo: ${self.salary}")
        print(f"Horas trabajadas: {self.hours_worked}")


lawyer = Job("Abogado", 1000, 6)
computer_teacher = Teacher(700, 18, "Computer Science", "Ayudante de laboratorio")
pediatric = Doctor(750, 24, "Pediatra", 40)

clear_screen()

print(color_me("Trabajos ⚖️ 📚 🩺\n", "yellow"))
lawyer.print_info()
print()
computer_teacher.print_info()
print()
pediatric.print_info()