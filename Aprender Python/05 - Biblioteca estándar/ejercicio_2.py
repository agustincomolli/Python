# Usar pip para instalar el paquete emoji: 
# - en Windows: py -m pip install emoji
# - en Linux: sudo pip install emoji
print("\nPaso 1: \n********")

import emoji
mensaje = emoji.emojize("¡Hola! ¡Hoy es un buen día :sun_with_face: para tomar unos :mate:!")
print(mensaje)