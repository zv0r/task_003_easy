#!/bin/bash

if [ -f ./src/Makefile ]; then
    cd src
fi

if [ -f Makefile ]; then
    if [ $(grep -i "\-Wall" ./Makefile 2>/dev/null | wc -l) -eq 0 ] || [ $(grep -i "\-Werror" ./Makefile 2>/dev/null | wc -l) -eq 0 ] || [ $(grep -i "\-Wextra" ./Makefile 2>/dev/null | wc -l) -eq 0 ]; then
        echo "You forgot the gcc options -Wall -Werror and -Wextra"
        exit 1
    fi 

    if [ $(grep -i "^ip_tools:" Makefile 2>/dev/null | wc -l) -eq 1 ]; then
        make ip_tools
    fi
fi
