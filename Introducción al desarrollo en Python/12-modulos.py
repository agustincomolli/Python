# Importar el módulo como espacio de nombre.
import modulo

modulo.mostrar("No es una alerta")

# Importar todas las funciones del espacio de nombre.
from modulo import *

mostrar("Otro mensaje")

# Importar funciones específicas dentro del espacio de nombre.
from modulo import mostrar

mostrar("Esta sí es una alerta", True)