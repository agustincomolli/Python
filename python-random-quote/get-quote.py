import random

def principal():
  #print("Mantenlo lógicamente impresionante.")

  archivo = open("citas.txt", encoding="UTF-8")
  citas = archivo.readlines()
  archivo.close()

  ultimo = len(citas) -1 # índice de la última cita.
  for i in range(3):
    num_aleatorio = random.randint(0, ultimo)
    print(f"{i + 1} - {citas[num_aleatorio].strip()}") # strip() elimina la línea en blanco.

  agregar_cita("Nada conquista excepto la verdad y la victoria de la verdad es el Amor. (San Agustín)")
  print("Agregar cita al archivo... completado.")

# Agregar una cita nueva al archivo de texto.
def agregar_cita(cita):
  with open("citas.txt", mode="a", encoding="UTF-8") as archivo:
    archivo.write("\n" + cita)

if __name__== "__main__":
  principal()
