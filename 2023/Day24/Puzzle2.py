import numpy as np
from itertools import combinations
from HailHelper import Stone

file = open("Input.txt", 'r')
input = file.read()
input = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
lines = input.split('\n')

stones = [Stone(line) for line in lines]

