from collections import defaultdict
from itertools import product

def tupAdd(a,b):
    return (a[0]+b[0], a[1]+b[1])

def get(grid, coord):
    return grid[coord[1]][coord[0]]

def isValid(grid, coord):
    if 0 <= coord[0] < len(grid[0]) and 0 <= coord[1] < len(grid):
        return get(grid, coord) in ".^v<>"
    return False

def getAdjacentCount(grid, coord):
    dirs = [(1,0), (-1,0), (0,-1), (0,1)]
    adjacent = [tupAdd(coord, d) for d in dirs if isValid(grid, tupAdd(coord, d))]
    return len(adjacent)

def getNeighbors(grid, coord):
    dirs = {'>': (1,0), '<': (-1,0), '^': (0,-1), 'v': (0,1)}
    uphill = {'v': '^', '^': 'v', '<': '>', '>': '<'}
    neighbors = {k: tupAdd(coord, d) for k,d in dirs.items() if isValid(grid, tupAdd(coord, d))}
    if (c := get(grid, coord)) in "<>^v":
        return [neighbors[c]]
    for k in list(neighbors.keys()):
        if get(grid, neighbors[k]) == uphill[k]:
            del neighbors[k]
    return neighbors.values()

def intersectionDist(intersections, neighbors, cur, end, dist, visited):
    if cur in intersections or cur == end:
        return (cur, dist)
    
    n = [p for p in neighbors[cur] if p not in visited][0]
    return intersectionDist(intersections, neighbors, n, end, dist+1, visited | {cur})

def calcPaths(graph, node, end, curDist, visited):
    if node == end:
        yield curDist
    
    for n, dist in graph[node]:
        if n in visited:
            continue
        yield from calcPaths(graph, n, end, curDist+dist, visited | {node})


file = open("Input.txt", 'r')
input = file.read()

grid = [[c for c in l] for l in input.split('\n')]
start = (grid[0].index('.'), 0)
end = (grid[-1].index('.'), len(grid)-1)

neighbors = defaultdict(list)
intersections = [start]
graph = defaultdict(list)

#the problem is that attempting to treat each location as its own vertex in a graph is unfeasible, as the sample alone has more than 200
#the key is to "roll up" paths so they only connect potentialk branching paths
for c in product(range(len(grid[0])), range(len(grid))):
    if not isValid(grid, c):
        continue
    n = getNeighbors(grid, c)
    neighbors[c].extend(n)
    #if there are at least 3 valid directions from this position then this is where a path intersects another
    #this is not necessarily equal to the number of neighbors because of how slopes work
    if getAdjacentCount(grid, c) >= 3:
        intersections.append(c)
    
for i in intersections:
    for n in neighbors[i]:
        val = intersectionDist(intersections, neighbors, n, end, 1, {i})
        graph[i].append(val)

paths = calcPaths(graph, start, end, 0, {start})
pathList = list(paths)
print(max(pathList))