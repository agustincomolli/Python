"""
Ejemplo del módulo loggin con distintos niveles.
"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    format=" %(asctime)s - %(levelname)s - %(message)s"
                    )

logging.debug("Algunos detalles menores de código y depuración.")
logging.info("Ocurrió un evento.")
logging.warning("Algo podría salir mal.")
logging.error("Se ha producido un error.")
logging.critical("¡El programa no puede recuperarse!")
