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

def dijkstra(start, end, vertices, edges):
    dist = defaultdict(lambda: math.inf)
    prev = defaultdict(lambda: [])
    unvisited = set(vertices)
    dist[start] = 0
    while unvisited:
        u = min(unvisited,key=lambda v: dist[v])
        unvisited.remove(u)
        for v,d in edges[u].items():
            tmp = dist[u] + d
            if tmp < dist[v]:
                dist[v] = tmp
                prev[v] = [u]
            elif tmp == dist[v]:
                prev[v].append(u)
    return dist, prev

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
                Vertices.append((dir,tuple(pos)))
                Edges[(dir,tuple(pos))][(rotate(dir,'CW'),tuple(pos))] = 1000
                Edges[(dir,tuple(pos))][(rotate(dir,'CCW'),tuple(pos))] = 1000
                if grid_get(grid,np.array([x,y])+arr) in 'SE.':
                    Edges[(dir,tuple(pos))][(dir,tuple(pos+arr))] = 1

start = get_terminus(grid,'S')
end = get_terminus(grid,'E')
dist, prev = dijkstra(('E',tuple(start)),('*',tuple(end)),Vertices,Edges)
check_verts = {('N',tuple(end))}
path_verts = {('N',tuple(end))}
while check_verts:
    vert = check_verts.pop()
    for v in prev[vert]:
        if v not in path_verts:
            path_verts.add(v)
            check_verts.add(v)
#for v in path_verts:
    #grid[v[1][1]][v[1][0]] = 'O'
#print('\n'.join([''.join(row) for row in grid]))
print(len({v[1] for v in path_verts}))
#print(sum(row.count('O') for row in grid))