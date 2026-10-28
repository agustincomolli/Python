"""
Diseña un script que simule el intento de conexión por red a un router 
inestable usando un bucle while.

Requerimientos:

1 - Solicitar al usuario el número máximo de reintentos permitidos (ej. 5).
2 - Dentro de un bucle while:
    * En cada intento, preguntar al operador en consola: 
      ¿El servidor respondió el ping? (s/n): .
    * Si responde "s", Imprimir: 
      "Conexión establecida con éxito en el intento <N>." 
      y romper el bucle inmediatamente (break).
    * Si responde "n", Mostrar: "Sin respuesta. Reintentando..." e 
      incrementar el contador de intentos.
3 - Si se alcanza el límite máximo de reintentos sin éxito, mostrar en pantalla: 
    "[FALLO CRÍTICO] Servidor inalcanzable tras <N> intentos."
"""

maximum_attempts = int(input("Intentos máximos: "))
count = 0
while count < maximum_attempts:
    count += 1

    responded = input("¿El servidor respondió el ping? (s/n): ").lower()
    if responded == "s":
        print(f"Conexión establecida con éxito en el intento {count}.")
        break

    print("Sin respuesta. Reintentando...")

if count == maximum_attempts:
    print(f"[FALLO CRÍTICO] Servidor inalcanzable tras {count} intentos.")
