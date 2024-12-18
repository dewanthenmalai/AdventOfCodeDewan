import math
from collections import defaultdict
from itertools import product
from scipy.cluster.hierarchy import DisjointSet

DIRS = [
    (0,-1),
    (0,1),
    (-1,0),
    (1,0)
]

with open('Input.txt','r') as file:
    lines = file.readlines()

coords = [tuple(int(c) for c in line.split(',')) for line in lines]
known = 1024
start = (0,0)
end = (70,70)

def valid(pos, dim):
    if len(pos) != len(dim):
        raise ValueError("Lengths are not equal")
    return all([0<=a<=b for a,b in zip(pos,dim)])

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
    return None, None

for i in range(known+1,len(coords)):
    print(i)
    s = DisjointSet([p for p in product(range(end[0]+1),range(end[1]+1)) if p not in coords[:i]])
    for pos in list(s):
        for dir in DIRS:
            next = tuple_add(pos,dir)
            if valid(next,end) and next not in coords[:i]:
                s.merge(pos,next)
    #print(s.subsets())
    if not s.connected(start,end):
        print(coords[i-1])
        break
