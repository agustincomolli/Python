#!/bin/bash

linea="-------------------------------------"

echo "Iniciado el: $(date)"; echo $linea
echo "Tiempo de encendido: "; uptime; echo $linea
echo "Memoria: "; free; echo $linea
echo "¿Quién está conectado?"; who; echo $linea
echo "Terminado el: $(date)"