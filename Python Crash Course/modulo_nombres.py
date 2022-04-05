def obtener_nombre_formateado(nombre, apellido,segundo_nombre=""):
    """Genera el nombre correctamente formateado."""
    if segundo_nombre:
        nombre_completo = f"{nombre} {segundo_nombre} {apellido}"
    else:
        nombre_completo = f"{nombre} {apellido}"
    
    return nombre_completo.title()