#!/bin/bash

# Verificamos si se ha pasado un parámetro al script
if [ -z "$1" ]; then
    echo "Por favor, indique el nombre de su aplicación Flask como parámetro."
    exit 1
fi

# Guardamos el nombre de la aplicación que se pasó como parámetro
app=$1

# Ejecutamos el servidor Flask directamente, permitiendo el acceso desde cualquier 
# IP y especificando la aplicación mediante la opción --app
flask --app $app run --host=0.0.0.0