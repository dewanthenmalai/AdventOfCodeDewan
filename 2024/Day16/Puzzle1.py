import math
import numpy as np
from collections import defaultdict

DIRS = {
    'N': np.array([0,-1]),
    'S': np.array([0,1]),
    'W': np.array([-1,0]),
    'E': np.array([1,0])
}
CHARS = {
    'N': '^',
    'S': 'v',
    'W': '<',
    'E': '>'
}

def rotate(dir, spin):
    CW = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }
    CCW = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }
    match spin:
        case 'CW':
            return CW[dir]
        case 'CCW':
            return CCW[dir]
        case _:
            raise ValueError(f'Unknown spin {spin}')

def grid_get(grid, pos):
        return grid[pos[1]][pos[0]]

def get_terminus(grid, val):
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == val:
                return np.array([x,y])

def manhattan(a, b):
    if len(a[1]) != len(b[1]):
        raise ValueError("Lengths are not equal")
    return sum(abs(i-j) for i,j in zip(a[1],b[1]))

def a_star(start, goal, edges, h):
    open = {start}
    prev = defaultdict(lambda: None)
    gScore = defaultdict(lambda: math.inf)
    gScore[start] = 0
    fScore = defaultdict(lambda: math.inf)
    fScore[start] = h(start,goal)
    while open:
        current = min(open,key=lambda v: fScore[v])
        if current[1] == goal[1]:
            return gScore, prev
        open.remove(current)
        for neighbor,cost in edges[current].items():
            tentative = gScore[current] + cost
            if tentative < gScore[neighbor]:
                prev[neighbor] = current
                gScore[neighbor] = tentative
                fScore[neighbor] = tentative + h(neighbor,goal)
                if neighbor not in open:
                    open.add(neighbor)
    return None

with open('Input.txt', 'r') as file:
    input = file.read()

grid = [[c for c in line.rstrip()] for line in input.rstrip().split('\n')]
Vertices = []
Edges = defaultdict(lambda: defaultdict(int))
for y,row in enumerate(grid):
    for x,c in enumerate(row):
        pos = np.array([x,y])
        if grid_get(grid,pos) in 'SE.':
            for dir,arr in DIRS.items():
                Vertices.append((dir,pos))
                Edges[(dir,tuple(pos))][(rotate(dir,'CW'),tuple(pos))] = 1000
                Edges[(dir,tuple(pos))][(rotate(dir,'CCW'),tuple(pos))] = 1000
                if grid_get(grid,np.array([x,y])+arr) in 'SE.':
                    Edges[(dir,tuple(pos))][(dir,tuple(pos+arr))] = 1

start = get_terminus(grid,'S')
end = get_terminus(grid,'E')
dist, prev = a_star(('E',tuple(start)),('*',tuple(end)),Edges,manhattan)
print(min([dist[('N',tuple(end))],dist[('S',tuple(end))],dist[('W',tuple(end))],dist[('E',tuple(end))]]))