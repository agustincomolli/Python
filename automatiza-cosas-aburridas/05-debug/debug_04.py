"""
Ejemplo del módulo loggin deshabilitando los mensajes.
"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    format=" %(asctime)s - %(levelname)s - %(message)s"
                    )

logging.critical("¡ERROR crítico, ERROR crítico!")
logging.disable(logging.CRITICAL)
logging.critical("¡ERROR crítico, ERROR crítico!")
logging.error("¡ERROR, ERROR!")
