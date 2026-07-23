import os
from mylib import color_me


def is_os_windows() -> bool:
    """
    Devuelve True si el Sistema Operativo es Windows.

    """
    
    if os.name == "nt":
        return True
    else:
        return False


def clear():
    """
    Limpia la pantalla.

    """

    if is_os_windows():
        os.system("cls")
    else:
        os.system("clear")


def mkdir(path: str):
    """
    Crear un directorio.

    """

    try:
        os.makedirs(path)
    except FileExistsError as error:
        path = color_me(path, "red")
        print(f"\nEl directorio '{path}' ya existe\n")


def cd(path: str):
    """
    Cambia de directorio.

    """

    os.chdir(path)


def ls(only_dir=False):
    """
    Muestra una lista de archivos y directorios.

    Args:
        only_dir (bool): Si es True muestra solamente los directorios.

    """

    if only_dir:
        # Imprimir solamente los directorios.
        for dir in os.listdir():
            if os.path.isdir(dir):
                print(color_me(dir, "blue"))
    else:
        # Imprimir los archivos y directorios.
        for file in os.listdir():
            if os.path.isdir(file):
                print(color_me(file, "blue"))
            else:
                print(file)


def pwd():
    """
    Imprime la ruta del directorio actual.

    """

    print(os.getcwd())


def rmdir(path: str):
    """
    Elimina un directorio o una rama de directorios.

    """

    try:
        os.removedirs(path)
    except FileNotFoundError:
        path = color_me(path, "red")
        print(
            f"\nEl sistema no puede encontrar el directorio especificado: '{path}'")
    except IOError:
        path = color_me(path, "red")
        print(f"\nEl sistema no puede eliminar el directorio: '{path}'")