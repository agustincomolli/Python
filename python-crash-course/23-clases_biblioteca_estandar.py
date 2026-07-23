from collections import OrderedDict
from typing import Dict

lenguajes_favoritos = OrderedDict()

lenguajes_favoritos["agustín"] = "python"
lenguajes_favoritos["gustavo"] = "visual basic"
lenguajes_favoritos["cacho"] = "turbo pascal"
lenguajes_favoritos["lorena"] = "cobol"
lenguajes_favoritos["carlitos"] = "python"

for nombre, lenguaje in lenguajes_favoritos.items():
    print(f"El lenguaje favorito de {nombre.title()} es " + \
        f"{lenguaje.capitalize()}."
    )