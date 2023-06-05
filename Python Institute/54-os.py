import os
import platform


def make_directory(path: str):
    """
    Crear un directorio.
    
    """
    
    try:
        os.mkdir(path)
    except FileExistsError as error:
        print(f"\nEl directorio '{path}' ya existe\n")


def change_directory(path: str):
    os.chdir(path)


def list_directory(only_dir=False):
    """
    Muestra una lista de archivos y directorios.

    Args:
        only_dir (bool): Si es True muestra solamente los directorios.

    """

    # Imprimir los archivos y directorios.
    if only_dir:
        for dir in os.listdir():
            print(dir)
    else:
        for file in os.listdir():
            if os.path.isdir(file):
                print(file)


def print_working_dir():
    """
    Imprime la ruta del directorio actual.

    """

    print(os.getcwd())


# Si el sistema operativo es Linux os.name devuelve "posix", sini "nt"
if os.name == "posix":
    print("Sistema Operativo Linux")
    print(platform.uname())
else:
    print("Sistema Operativo Windows")
    print(platform.uname())

make_directory("./my_directory")

list_directory(only_dir=True)

change_directory("./my_directory")

print_working_dir()