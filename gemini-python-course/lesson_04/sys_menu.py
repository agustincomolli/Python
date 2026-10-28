"""
Consola Interactiva de Soporte IT (sys_menu.py)
Crea un script que despliegue un menú de opciones para un operador de 
Helpdesk. El programa debe repetirse continuamente hasta que el usuario 
elija salir.

Requerimientos:

1 - Desplegar el siguiente menú dentro de un bucle while:

    Plaintext
    === MENU DE ADMINISTRACION DE SISTEMAS ===
    1. Verificar estado de servicio
    2. Reiniciar servicio
    3. Salir

2 - Capturar la opción ingresada por el usuario:
    - Si elige 1: Mostrar en consola "Servicio evaluado: RUNNING (OK)".
    - Si elige 2: Mostrar "Reiniciando servicio... Servicio REINICIADO con 
      exito".
    - Si elige 3: Imprimir "Cerrando consola de administración..." y finalizar 
      el programa usando break.
    - Si escribe cualquier otra opción: Mostrar "Opción no válida. Intente 
      nuevamente." y volver a presentar el menú.
"""

option = 0

while option != 3:
    print(
        "=== MENU DE ADMINISTRACION DE SISTEMAS ===\n"
        "\n1. Verificar estado de servicio"
        "\n2. Reiniciar servicio"
        "\n3. Salir\n"
    )

    option = int(input("Elija una opción: "))

    if option == 1:
        print("\nServicio evaluado: RUNNING (OK)")
    elif option == 2:
        print("\nReiniciando servicio... Servicio REINICIADO con exito")
    elif option == 3:
        break
    else:
        print("\nOpción no válida. Intente nuevamente.")

    input("\nPresione ENTER para continuar...")
