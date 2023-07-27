# En una clase faltó el profesor y uno de los alumnos lo sustituirá.
# 1 - Pedir la edad de los compañeros que asistieron a la clase y ordenarlos
# de menor a mayor.
# 2 - El mayor será el profesor y el menor el alumno. ¿Quién es quién?

def get_students() -> list:
    """
    Obtiene una lista de estudiantes junto con sus nombres y edades.

    Retorna:
        list: Una lista de diccionarios, donde cada diccionario representa a 
             un estudiante y contiene las siguientes claves:
            - name (str): El nombre del estudiante.
            - age (int): La edad del estudiante.
    """

    students = []
    is_done = False

    print(f"Listado de estudiantes\n{'*'* 22}")

    while not is_done:
        # Crear un diccionario con los datos del alumno en cada iteración
        # porque sino todas las referencias de la lista apuntarían al mismo
        # diccionario y tendría una lista con todos los diccionarios iguales.
        student = {"name": None, "age": None}

        student["name"] = input("Nombre: ")
        student["age"] = int(input("Edad: "))
        students.append(student)

        answer = input("¿Desea agregar otro? [S|N]: ").lower()
        is_done = answer != "s"

    return students


def identify_profesor(students: list) -> str:
    """
    Identifica al profesor de la clase siendo el alumno de mayor edad.

    Retorna:
        str: El nombre del profesor.
    """

    # Ordenar la lista de estudiantes por edad
    # Usamos una función lambda para especificar la clave por la que queremos 
    # ordenar los diccionarios. En este caso, student representa cada diccionario 
    # dentro de la lista students, y student["age"] se utiliza para acceder al valor 
    # de la clave "age" en cada diccionario. La función lambda devuelve el valor 
    # de "age" como base para la ordenación.
    students.sort(key=lambda student: student["age"])

    return students[-1]["name"]

professor = identify_profesor(get_students())
print(f"\nEl profesor es {professor}.")
