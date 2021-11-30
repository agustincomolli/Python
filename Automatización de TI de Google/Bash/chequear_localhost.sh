#/bin/bash

if grep "127.0.0.1" /etc/hosts
then
    echo "Todo está bien."
else
    echo "¡ERROR!: no se encuentra la entrada 127.0.0.1 en el archivo /etc/hosts"
fi