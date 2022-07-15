import shutil
import os
from pathlib import Path

directorio = Path("D:/Users/Agustín/Cursos/Python/Automatiza cosas aburridas")

# Copiar un archivo.
resultado = shutil.copy(directorio / "soneto.txt", directorio / 
                        "43-carpeta/copia de soneto.txt")
print(f"¡Archivo copiado con éxito!\n---> {resultado}\n")

# Copiar un directorio
resultado = shutil.copytree(directorio / "43-carpeta", directorio / 
                            "43-copia_carpeta", dirs_exist_ok=True)
print(f"¡Carpeta copiada con éxito!\n---> {resultado}\n")

# Mover un archivo y renombrarlo.
resultado = shutil.move(directorio / "43-copia_carpeta/copia de soneto.txt",
                        directorio / "backup de soneto.txt")
print(f"¡El archivo se ha movido a la nueva ubicación!\n---> {resultado}\n")

# Eliminar un archivo.
os.unlink(directorio / "backup de soneto.txt")
print("El archivo ha sido eliminado.\n")