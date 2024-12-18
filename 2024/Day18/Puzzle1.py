import math
from collections import defaultdict
from itertools import product

DIRS = [
    (0,-1),
    (0,1),
    (-1,0),
    (1,0)
]

with open('Input.txt','r') as file:
    lines = file.readlines()

coords = [tuple(int(c) for c in line.split(',')) for line in lines]
limit = 1024
sample = coords[:limit]
start = (0,0)
end = (70,70)

def tuple_add(a,b):
    if len(a) != len(b):
        raise ValueError("Lengths are not equal")
    return tuple(i+j for i,j in zip(a,b))

def manhattan(a, b):
    if len(a) != len(b):
        raise ValueError("Lengths are not equal")
    return sum(abs(i-j) for i,j in zip(a,b))

def a_star(start, goal, edges, h):
    open = {start}
    prev = defaultdict(lambda: None)
    gScore = defaultdict(lambda: math.inf)
    gScore[start] = 0
    fScore = defaultdict(lambda: math.inf)
    fScore[start] = h(start,goal)
    while open:
        current = min(open,key=lambda v: fScore[v])
        if current == goal:
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

Vertices = []
Edges = defaultdict(dict)
for pos in product(range(end[0]+1),range(end[1]+1)):
    if pos not in sample:
        Vertices.append(pos)
        for dir in DIRS:
            if tuple_add(pos,dir) not in sample:
                Edges[pos][tuple_add(pos,dir)] = 1

dist, prev = a_star(start, end, Edges, manhattan)
print(dist[end])