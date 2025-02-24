#!/bin/bash

if [ ! -e "$1/README.md" ] ; then
    echo "# [Round $1](https://codeguessing.gay/$1/): 

[*Submitted entry*](https://codeguessing.gay/$1/#)

*Relevant files:* ``" > "$1/README.md"
fi
echo done