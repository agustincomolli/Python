# Convertidor de Markdown a PDF

Este proyecto proporciona una herramienta simple para convertir archivos Markdown a PDF utilizando Python.

## Descripción

El script `markdown_to_pdf.py` convierte archivos Markdown (.md) a formato PDF. Utiliza las bibliotecas `mistune` para renderizar Markdown a HTML y `weasyprint` para generar el PDF a partir del HTML.

## Características

- Convierte archivos Markdown a PDF
- Soporta estilos personalizados mediante archivos CSS
- Fácil de usar desde la línea de comandos

## Requisitos

- Python 3.x
- mistune
- weasyprint
- cssutils

## Instalación

1. Clona este repositorio o descarga el script `markdown_to_pdf.py`.
2. Instala las dependencias necesarias:

```
pip install mistune weasyprint cssutils
```

## Uso

### Desde la línea de comandos

```
python markdown_to_pdf.py archivo_entrada.md archivo_salida.pdf [archivo_css]
```

Ejemplo:
```
python markdown_to_pdf.py mi_documento.md mi_documento.pdf
```

### Como módulo en tu propio código

```python
from markdown_to_pdf import markdown_to_pdf

markdown_to_pdf('mi_documento.md', 'mi_documento.pdf', 'estilos.css')
```

## Personalización

Puedes personalizar el estilo del PDF resultante proporcionando un archivo CSS como tercer argumento al llamar al script o a la función `markdown_to_pdf`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos o crea un pull request directamente.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` en el repositorio para más detalles.

```
MIT License

Copyright (c) [año] [nombre completo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
