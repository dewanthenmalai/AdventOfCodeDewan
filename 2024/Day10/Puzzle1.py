import numpy as np

DIRS = [
    np.array([0,-1]),
    np.array([0,1]),
    np.array([1,0]),
    np.array([-1,0])
]

def grid_get(grid,loc):
    if 0 <= loc[0] < len(grid[0]) and 0 <= loc[1] < len(grid):
        return grid[loc[1]][loc[0]]
    return None

def get_trailheads(grid):
    retList = []
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == 0:
                retList.append(np.array([j, i]))
    return retList

def get_endpoints(grid,loc,ends):
    if grid_get(grid,loc) == 9:
        ends.add(tuple(loc))
        return
    for dir in DIRS:
        if grid_get(grid,loc+dir) is not None and grid_get(grid,loc+dir) == grid_get(grid,loc)+1:
            get_endpoints(grid,loc+dir,ends)
    return ends

with open('Input.txt', 'r') as file:
    lines = file.readlines()

grid = [[int(c) if c.isdigit() else c for c in line.rstrip()] for line in lines]
trailheads = get_trailheads(grid)

ends = []
for trailhead in trailheads:
    tmp = set()
    get_endpoints(grid,trailhead,tmp)
    ends.append(tmp)

print(sum([len(e) for e in ends]))