"""
En scripts de automatización reales, queremos ver progreso en tiempo real sin 
que llene la pantalla de líneas nuevas.

Escribe tres líneas de código independientes (tres instrucciones print()).

Las tres deben ejecutarse de manera que en la consola final todo se imprima en 
una sola línea continua, simulando que la barra avanzó.

El resultado final en pantalla debe ser:

Plaintext
[CONECTANDO]... [PROCESANDO BACKUP]... ██████████ 100% [COMPLETO]
"""

print("[CONECTANDO]...", end=" ")
print("[PROCESANDO BACKUP]...", end=" ")
print("██████████ 100% [COMPLETO]")
