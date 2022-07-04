#! python3

# Crea cuestionarios con preguntas y respuestas en orden aleatorio, junto
# con la clave de respuesta.

from ctypes import resize
import random

capitales = {
                "Buenos Aires": "La Plata",
                "Catamarca": "San Fernando del Valle de Catamarca",
                "Chaco": "Resistencia",
                "Chubut": "Rawson",
                "Córdoba": "Córdoba",
                "Corrientes": "Corrientes",
                "Entre Ríos": "Paraná",
                "Formosa": "Formosa",
                "Jujuy": "San Salvador de Jujuy",
                "La Pampa": "Santa Rosa",
                "La Rioja": "La Rioja",
                "Mendoza": "Mendoza",
                "Misiones": "Posadas",
                "Neuquén": "Neuquén",
                "Río Negro": "Viedma",
                "Salta": "Salta",
                "San Juan": "San Juan",
                "San Luis": "San Luis",
                "Santa Cruz": "Río Gallegos",
                "Santa Fe": "Santa Fe",
                "Santiago del Estero": "Santiago del Estero",
                "Tierra del Fuego, Antártida e Islas del Atlántico Sur": 
                    "Ushuaia",
                "Tucumán": "San Miguel de Tucumán"
            }

# Generar 35 archivos de prueba.
for num_examen in range(5):
    # Crear los archivos con las preguntas y respuestas.
    archivo_examen = open(f"examen-{num_examen + 1}.txt", mode="w", 
                          encoding="UTF-8")
    archivo_respuestas = open(f"examen-{num_examen + 1} - respuestas.txt", 
                              mode="w", encoding="UTF-8")
    
    # Escribir el encabezado del examen.
    archivo_examen.write("Nombre:\n\nFecha:\n\nPeríodo:\n\n")
    archivo_examen.write(f"{' ' * 20} Examen sobre capitales de provincia " +
                         f"(Examen N°: {num_examen + 1})\n\n")

    # Mezclar el orden de las provincias.
    provincias = list(capitales.keys())
    random.shuffle(provincias)

    # Recorrer las provincias y hacer preguntas para cada una.
    for num_pregunta in range(len(provincias)):
        # Obtener respuestas correctas e incorrectas.
        resp_correcta = capitales[provincias[num_pregunta]]
        resp_incorrectas = list(capitales.values())
        del resp_incorrectas[resp_incorrectas.index(resp_correcta)]
        # Elegir 3 respuestas incorrectas al azar para esta pregunta.
        resp_incorrectas = random.sample(resp_incorrectas, 3)
        opciones_respuesta = resp_incorrectas + [resp_correcta]
        random.shuffle(opciones_respuesta)

        # Escribir la pregunta con las opciones de respuesta en el archivo.
        pregunta = f"{num_pregunta + 1} - "
        pregunta += f"¿Cuál es la capital de {provincias[num_pregunta]}?\n"
        archivo_examen.write(pregunta)
        for num_respuesta in range(len(opciones_respuesta)):
            opcion = f"    {'ABCD'[num_respuesta]} - "
            opcion += f"{opciones_respuesta[num_respuesta]}\n"
            archivo_examen.write(opcion)

        archivo_examen.write("\n")

        # Escribir la respuesta correcta en el archivo de respuestas.
        respuesta = f"{num_pregunta + 1} - "
        respuesta += f"[ {'ABCD'[opciones_respuesta.index(resp_correcta)]} ] "
        respuesta += f"{opciones_respuesta[num_respuesta]}\n"
        archivo_respuestas.write(respuesta)
        
    # Cerrar los archivos.
    archivo_examen.close()
    archivo_respuestas.close()