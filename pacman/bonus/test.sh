#!/bin/bash

python3 pacman.py map1 '+' ' '

gcc -o test main.c -lncurses

./test map1 post