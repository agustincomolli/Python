import sys
from os import strerror


def copy_file(src_path:str, dst_path:str):
    try:
        src_file = open(src_path, mode="rb")
    except IOError as e:
        print(f"No se puede abrir el archivo de origen: {strerror(e.errno)}")
        exit(e.errno)
    
    try:
        dst_file = open(dst_path, "wb")
    except IOError as e:
        print(f"No se puede crear el archivo de destino: {strerror(e.errno)}")
        src_file.close()
        exit(e.errno)

    buffer = bytearray(65536)
    try:
        while True:
            data = src_file.readinto(buffer)
            
            if not data:
                break

            dst_file.write(buffer[:data])
    except IOError as e:
        print(f"Ocurrió un error al copiar el archivo {strerror(e.errno)}.")
        exit(e.errno)

    print("Archivo copiado!")
    src_file.close()
    dst_file.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python copy_file.py <ruta_origen> <ruta_destino>")
    else:
        source_path = sys.argv[1]
        destination_path = sys.argv[2]
        copy_file(source_path, destination_path)