@echo off
REM Comprobar si se pasó un parámetro al script
IF "%~1"=="" (
    echo Por favor, indique el nombre de su aplicación Flask como parámetro.
    exit /b
)

REM Ejecutar el servidor Flask directamente, permitiendo el acceso desde cualquier IP
REM  y especificando la aplicación mediante la opción --app
flask --app=%~1 run --host=0.0.0.0