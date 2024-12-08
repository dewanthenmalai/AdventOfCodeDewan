import numpy as np
from itertools import combinations

def index_2D(list, elem):
    retList = []
    for i, x in enumerate(list):
        for j in range(len(x)):
            if list[i][j] == elem:
                retList.append(np.array([j, i]))
    return retList

def is_in(pos, grid):
    return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < [len(grid)]

def get_antinode_line(pair, grid):
    antinodes = []
    slope = pair[0] - pair[1]
    loc = pair[0]
    while is_in(loc, grid):
        antinodes.append(loc)
        loc = loc + slope
    loc = pair[0]
    while is_in(loc, grid):
        antinodes.append(loc)
        loc = loc - slope
    return antinodes

def get_antinodes(grid, freq):
    antennas = index_2D(grid, freq)
    pairs = combinations(antennas, 2)
    antinodes = []
    for pair in pairs:
        antinodes.extend(get_antinode_line(pair,grid))
    return {tuple(antinode) for antinode in antinodes}
    
    

with open('Input.txt', 'r') as file:
    lines = file.readlines()

grid = [[c for c in line.rstrip()] for line in lines]
freqs = set([x for xs in grid for x in xs])
freqs.remove('.')
antinode_locs = set()

for freq in freqs:
    antinode_locs.update(get_antinodes(grid,freq))

print(len(antinode_locs))