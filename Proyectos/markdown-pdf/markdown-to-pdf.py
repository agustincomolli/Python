"""
Convertidor de Markdown a PDF
"""
import sys
import mistune
import weasyprint
import cssutils


def markdown_to_pdf(markdown_file, pdf_file, css_file=None):
    """Convierte un archivo Markdown a PDF.

    Args:
      markdown_file (str): Ruta al archivo Markdown.
      pdf_file (str): Ruta donde se guardará el PDF.
      css_file (str, opcional): Ruta al archivo CSS para personalizar el estilo.

    Returns:
      None
    """

    # Lee el contenido del archivo Markdown
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # Renderiza el Markdown a HTML
    html = mistune.markdown(markdown_text)

    # Crea un objeto CSS para personalizar el estilo
    stylesheets = []
    if css_file:
        sheet = cssutils.parseFile(css_file)
        stylesheets.append(sheet)

    # Crea el PDF
    weasyprint.HTML(string=html, stylesheets=stylesheets).write_pdf(pdf_file)


if __name__ == "__main__":
    # Si no se proporcionaron los argumentos válidos mostrar un mensaje de uso
    if not len(sys.argv) < 3:
        print("# Ejemplo de uso:\n" +
              "markdown_to_pdf('mi_documento.md', 'mi_documento.pdf')")
    else:
        markdown_to_pdf(sys.argv[1], sys.argv[2])
