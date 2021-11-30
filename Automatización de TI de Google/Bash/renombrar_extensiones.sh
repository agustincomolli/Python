#!/bin/bash

# Crear archivos para trabajar.
touch about.htm contact.htm footer.htm header.htm index.htm
ls *.h*

for archivo in *.htm; do
    # basename devuelve el nombre del archivo sin su extensión.
    nombre=$(basename "$archivo" .htm)
    echo renombrar "$archivo" a "$nombre.html"
    # renombrar archivo.
    mv "$archivo" "$nombre.html"
done

ls *.h*