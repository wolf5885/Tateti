#!/usr/bin/env python3

from interface_a import createBoard
from helpers import *

print("====TATETI====")

game = input("Quiere comenzar a jugar (S/N)?: ")
clearScreen()
board = createBoard()

for linea in board:
	print(linea)
