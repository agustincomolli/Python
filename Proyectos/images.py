"""
Este módulo proporciona una interfaz gráfica de usuario (GUI) para convertir imágenes 
a formato WebP y redimensionarlas. Utiliza `tkinter` para la GUI y `Pillow` para el 
procesamiento de imágenes.

Funciones:
- convert_to_webp(input_path, output_path=None): Convierte una imagen a formato WebP.
- resize_image(input_path, output_path=None, new_size=(100, 100)): Redimensiona una imagen.
- select_files(): Abre un cuadro de diálogo para seleccionar múltiples archivos de imagen.
- convert_and_resize(): Convierte y redimensiona las imágenes seleccionadas.
"""

import tkinter as tk
import os
from tkinter import filedialog, messagebox
from PIL import Image


def convert_to_webp(input_path, output_path=None):
    """
    Convierte una imagen en formato WebP.

    Args:
        input_path (str): Ruta de entrada de la imagen.
        output_path (str, optional): Ruta de salida donde se guardará la imagen convertida. 
            Si no se proporciona, la imagen se guarda temporalmente en 'temp.webp'.

    Returns:
        PIL.Image.Image or None: Si no se proporciona un 'output_path', retorna el objeto 
        de imagen convertido. Si se proporciona 'output_path', no retorna nada.

    Raises:
        FileNotFoundError: Si no se encuentra el archivo en 'input_path'.
        OSError: Si ocurre un error al abrir o guardar la imagen.

    """
    try:
        image = Image.open(input_path)
        if output_path:
            image.save(output_path, 'webp')
            print(f"Imagen convertida y guardada en {output_path}")
        else:
            image.save('temp.webp', 'webp')
            return Image.open('temp.webp')
    except FileNotFoundError:
        print(f"Archivo no encontrado: {input_path}")
    except OSError as e:
        print(f"Error al abrir o guardar la imagen: {e}")


def resize_image(input_path, output_path=None, new_size=(100, 100)):
    """
    Redimensiona una imagen.

    Args:
        input_path (str): Ruta de entrada de la imagen.
        output_path (str, optional): Ruta de salida donde se guardará la imagen redimensionada. 
            Si no se proporciona, la imagen redimensionada se retorna como un objeto 
            PIL.Image.Image.
        new_size (tuple, optional): Tamaño nuevo de la imagen como una tupla (ancho, alto). 
            Por defecto es (100, 100).

    Returns:
        PIL.Image.Image or None: Si no se proporciona un 'output_path', retorna el objeto de imagen 
        redimensionada. Si se proporciona 'output_path', no retorna nada.

    Raises:
        FileNotFoundError: Si no se encuentra el archivo en 'input_path'.
        ValueError: Si hay un problema con el valor de 'new_size'.
        OSError: Si ocurre un error al abrir o guardar la imagen.

    """
    try:
        image = Image.open(input_path)
        if output_path:
            resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
            resized_image.save(output_path)
            print(f"Imagen redimensionada y guardada en {output_path}")
        else:
            return image.resize(new_size, Image.Resampling.LANCZOS)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {input_path}")
    except ValueError as e:
        print(f"Valor incorrecto: {e}")
    except OSError as e:
        print(f"Error al abrir o guardar la imagen: {e}")


def select_files():
    """
    Abre un cuadro de diálogo para seleccionar múltiples archivos de imagen.

    Actualiza la lista de archivos seleccionados.
    """
    title = "Selecciona las imágenes"
    filetypes = [("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    file_paths = filedialog.askopenfilenames(title=title, filetypes=filetypes)
    if file_paths:
        input_paths.set(";".join(file_paths))
        file_listbox.delete(0, tk.END)
        for file_path in file_paths:
            file_listbox.insert(tk.END, file_path)


def convert_and_resize():
    """
    Convierte y redimensiona las imágenes seleccionadas.

    Obtiene las rutas de las imágenes desde input_paths, las convierte a formato WebP
    y las redimensiona al tamaño especificado en width_entry y height_entry. Si no se
    especifica tamaño, mantiene el tamaño original.

    Muestra un mensaje de éxito o error según el resultado.
    """
    try:
        files = input_paths.get().split(";")
        width = width_entry.get()
        height = height_entry.get()

        if not width or not height:
            new_size = None
        else:
            new_size = (int(width), int(height))

        for file_path in files:
            output_path = os.path.splitext(file_path)[0] + ".webp"
            convert_to_webp(file_path, output_path)
            if new_size:
                resize_image(output_path, output_path, new_size)

        messagebox.showinfo(
            "Éxito", "Las imágenes han sido convertidas y redimensionadas exitosamente.")
    except FileNotFoundError:
        messagebox.showerror(
            "Error", "No se encontró uno de los archivos seleccionados.")
    except ValueError:
        messagebox.showerror(
            "Error", "Valor incorrecto para el tamaño de la imagen.")
    except OSError as e:
        messagebox.showerror(
            "Error", f"Ocurrió un error al abrir o guardar la imagen: {e}")


# Crear la interfaz gráfica
root = tk.Tk()
root.title("Conversión y Redimensionado de Imágenes")

input_paths = tk.StringVar()

# Botón para seleccionar archivos
tk.Button(root, text="Seleccionar Imágenes",
          command=select_files).pack(pady=10)

# Lista para mostrar las rutas seleccionadas
file_listbox = tk.Listbox(root, width=50, height=10)
file_listbox.pack(pady=5)

# Campos para el tamaño nuevo
tk.Label(root, text="Ancho:").pack(pady=5)
width_entry = tk.Entry(root)
width_entry.pack(pady=5)

tk.Label(root, text="Alto:").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Botón para convertir y redimensionar
tk.Button(root, text="Convertir y Redimensionar",
          command=convert_and_resize).pack(pady=20)

root.mainloop()
