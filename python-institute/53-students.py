from os import strerror


class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    def __init__(self, line_number:int):
        super().__init__(self)
        self.line_number = line_number


class FileEmpty(StudentsDataException):
    pass


def create_studient_dict(file_name: str) -> dict:
    """
    Crea un diccionario con el nombre y apellido del estudiante como clave y
    la suma de todos los puntos como valor.

    Args:
        file_name (str): Nombre del archivo.

    Returns: Diccionario

    """

    student_list = {}

    try:
        with open(file_name, mode="r", encoding="UTF-8") as file:
            # Verificar que el archivo no esté vacío.
            lines = file.readlines()
            line_number = 0
            if len(lines) == 0:
                raise FileEmpty

            for line in lines:
                line_number += 1
                student = line.split()

                # Verificar que tenga 3 campos por registro.
                if len(student) != 3:
                    raise WrongLine(line_number)

                name = f"{student[0]} {student[1]}"
                # Verificar que el último campo sea un número.
                try:
                    if name in student_list:
                        student_list[name] += float(student[2])
                    else:
                        student_list[name] = float(student[2])
                except ValueError:
                    raise WrongLine

        return student_list
    except WrongLine as error:
        message = "Error: el registro del estudiante de la línea "
        message += f"{error.line_number} no tiene los datos requeridos."
        print(message)
        exit()
    except FileEmpty as error:
        print("Error: el archivo está vacío.")
        exit()
    except IOError as error:
        print("Error: no se puede abrir el archivo.")
        exit()


def show_resume(students: dict):
    """
    Imprime en pantalla el nombre del estudiante y su puntaje ordenados por
    nombre de estudiante.

    Args:
        students (dict): diccionario que tiene los datos a mostrar.
        
    """

    # Ordenar el diccionario por nombre.
    students_sorted = sorted(students.items(), key=lambda x: x[0])
    for student_name, student_points in students_sorted:
        print(f"{student_name}:\t{student_points}")


file_name = input("Ingrese el nombre del archivo: ")
student_dict = create_studient_dict(file_name)
show_resume(student_dict)
