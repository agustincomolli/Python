#!/bin/bash

for archivo_log in /var/log/*.log; do
    echo "Procesando $archivo_log"
    cut -d" " -f5- $archivo_log | sort | uniq -c | sort -nr | head -5
done