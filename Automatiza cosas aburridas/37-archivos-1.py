from pathlib import Path

print("1 - Listar archivos:")
lista_archivos = ["archivo1.docx", "archivo2.xlsx", "archivo3.pptx", "archivo4.pdf"]
for archivo in lista_archivos:
    print(Path(r"C:/Users/Usuario/Documents", archivo))

# Ver el directorio de trabajo actual.
print("\n2 - Directorio de trabajo actual:")
print(Path.cwd())