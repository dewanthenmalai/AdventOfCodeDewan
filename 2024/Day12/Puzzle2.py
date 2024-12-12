from collections import deque
from copy import copy
from itertools import combinations
from tqdm import tqdm

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

def tuple_add(a, b):
    return (a[0]+b[0],a[1]+b[1])

def tuple_get(grid, loc):
    if 0 <= loc[0] < len(garden[0]) and 0 <= loc[1] < len(garden):
        return garden[loc[1]][loc[0]]
    return None

def get_region(garden, loc):
    region = {loc}
    plant = tuple_get(garden, loc)
    next = [tuple_add(loc,dir) for dir in DIRS]
    i = 0
    while i < len(next):
        if next[i] not in region and tuple_get(garden, next[i]) == plant:
            region.add(next[i])
            next.extend([tuple_add(next[i],dir) for dir in DIRS])
        i += 1
    return region

def get_edge_segments(region):
    return {frozenset([sq,tuple_add(sq,dir)]) for dir in DIRS for sq in region if tuple_add(sq,dir) not in region}

def get_corner_count(region):
    corners = 0
    for x,y in region:
        corners += sum(((x, y+dy) not in region and (x+dx, y) not in region) or 
                    ((x, y+dy) in region and (x+dx, y) in region and (x+dx, y+dy) not in region)
                    for dx in (1,-1) for dy in (1,-1))
    return corners

def get_sides(region):
    total = 0
    return total

with open('Input.txt', 'r') as file:
    lines = file.readlines()

garden = [[c for c in line.rstrip()] for line in lines]

regions = []
checked = set()
for j, row in enumerate(garden):
    for i in range(len(row)):
        if (i,j) in checked:
            continue
        region = get_region(garden,(i,j))
        regions.append(region)
        checked |= region

price = 0
corners = []
for region in tqdm(regions):
    area = len(region)
    corner_count = get_corner_count(region)
    corners.append(corner_count)
    price += area * corner_count

print(price)