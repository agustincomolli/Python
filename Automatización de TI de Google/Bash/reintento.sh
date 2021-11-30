#!/bin/bash

n=0
comando=$1
while ! $comando && [ $n -le 5 ]; do
    sleep $n
    ((n+=1))
    echo "Reintento $n"
done;