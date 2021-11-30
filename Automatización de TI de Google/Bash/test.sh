#!/bin/bash

# test -n "variable" chequea que si una variable string está vacía.
if test -n "$PATH"; then echo "La variable PATH no está vacía."; fi

# Otra forma más corta.
if [ -n "$PATH" ]; then echo "La variable PATH no está vacía."; fi