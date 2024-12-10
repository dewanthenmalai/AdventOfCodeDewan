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

def get_unique_path_count(grid,loc):
    if grid_get(grid,loc) == 9:
        return 1
    paths = [get_unique_path_count(grid,loc+dir) for dir in DIRS if grid_get(grid,loc+dir) == grid_get(grid,loc)+1]
    return sum(paths)

with open('Input.txt', 'r') as file:
    lines = file.readlines()

grid = [[int(c) if c.isdigit() else c for c in line.rstrip()] for line in lines]
trailheads = get_trailheads(grid)

ratings = []
for trailhead in trailheads:
    ratings.append(get_unique_path_count(grid,trailhead))

print(sum(ratings))