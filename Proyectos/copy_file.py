import os
import sys


def copy_file(src_path: str, dst_path: str):
    """
    Copia un archivo.
    
    Args:
        src_path (str): La ruta y el nombre del archivo de origen.
        dst_path (str): La ruta y el nombre del archivo de destino.

    """

    # Verificar si el archivo de origen existe.
    if not os.path.exists(src_path):
        print(f"El archivo de origen {src_path} no existe.")
        return

    try:
        with open(src_path, mode="rb") as src_file, open(dst_path, mode="wb") as dst_file:
            while True:
                # Leer un bloque de datos del archivo de origen
                data = src_file.read(65536)

                if not data:
                    break

                # Escribir el bloque de datos en el archivo de destino
                dst_file.write(data)
            
            print("¡Archivo copiado!")
    except Exception as error:
        print(f"Ocurrió un error al copiar el archivo: {error}")
    pass


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python copy_file.py <ruta_origen> <ruta_destino>")
    else:
        source_path = sys.argv[1]
        destination_path = sys.argv[2]
        copy_file(source_path, destination_path)
