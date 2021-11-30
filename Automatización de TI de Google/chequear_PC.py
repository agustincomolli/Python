#!/usr/bin/env python3
import shutil, psutil
from network import *

def chequear_espacio_disco(disco):
    espacio_disco = shutil.disk_usage(disco)
    espacio_libre = espacio_disco.free / espacio_disco.total * 100
    return espacio_libre > 20

def chequear_uso_cpu():
    uso_cpu = psutil.cpu_percent(1)
    return uso_cpu < 75

if not chequear_espacio_disco("/") or not chequear_uso_cpu:
    print("¡ERROR!")
elif check_localhost() and check_connectivity():
    print("Todo está bien.")
else:
    print("Las comprobaciones de red fallaron")