def saludar_usuario(nombre_usuario):
    """Muestra un saludo simple."""
    print(f"¡Hola {nombre_usuario.capitalize()}!")

saludar_usuario("agustín")

def describir_mascota(nombre_mascota, tipo_animal="perro"):
    """Muestra información acerca de la mascota."""
    # Cuando utiliza valores predeterminados, cualquier parámetro 
    # con un valor predeterminado debe aparecer en la lista después 
    # de todos los parámetros que no tienen valores predeterminados. 
    # Esto permite que Python continúe interpretando correctamente 
    # los argumentos posicionales.
    print(f"\nTengo un {tipo_animal}.")
    print(f"Mi {tipo_animal} se llama {nombre_mascota.capitalize()}.")

# Usar argumentos posicionales.
describir_mascota("perro", "mendieta")
# Usar argumentos por valor.
describir_mascota(tipo_animal="gato", nombre_mascota="pancha")
describir_mascota(nombre_mascota="verdurita", tipo_animal="tortuga")
describir_mascota(nombre_mascota="chingola")