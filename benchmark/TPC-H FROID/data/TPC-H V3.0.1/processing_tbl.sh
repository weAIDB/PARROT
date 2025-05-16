#!/bin/bash

mkdir -p tbl

for i in *.tbl
do
    name="tbl/$i"
    echo $name
    touch $name
    chmod 644 $name
    sed 's/|$//' "$i" >> "$name"
done