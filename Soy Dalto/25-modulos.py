import mis_funciones

# Importar módulos que están en otras rutas.
import sys
sys.path.append("D:/Users/Agustín/Cursos/Python/Proyectos")
from mylib import color_me

mis_funciones.greetings(color_me("Agustín", "green"))

# Acceder al nombre de este módulo.
print(__name__)
# Acceder al nombre del módulo importado.
print(mis_funciones.__name__)