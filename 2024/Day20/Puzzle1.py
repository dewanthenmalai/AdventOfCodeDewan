from collections import defaultdict

DIRS = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
]

def tuple_add(a,b):
    if len(a) != len(b):
        raise ValueError('Tuples have different lengths')
    return tuple(e1+e2 for e1,e2 in zip(a,b))

def tuple_mult(tup, scalar):
    return tuple(i*scalar for i in tup)

def grid_get(grid, pos):
    if 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid):
        return grid[pos[1]][pos[0]]
    raise ValueError(f'Index out of bounds for {pos} with grid dimensions ({len(grid[0])}, {len(grid)})')

def get_terminus(grid, val):
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == val:
                return (x,y)
    return None

def evaluate_shortcut(pos, dir, path, grid):
    next = tuple_add(pos,dir)
    after = tuple_add(next,dir)
    if after not in path:
        return False
    is_wall = grid_get(grid,next) == '#'
    is_path = grid_get(grid,after) in 'E.'
    forward = path.index(pos) < path.index(after)
    return is_wall and is_path and forward

with open('Input.txt','r') as file:
    input = file.readlines()

grid = [[c for c in line.rstrip()] for line in input]

start = get_terminus(grid, 'S')
end = get_terminus(grid, 'E')
pos = start
path = [start]
while pos != end:
    for dir in DIRS:
        next = tuple_add(pos,dir)
        if grid_get(grid,next) in 'SE.' and next not in path:
            path.append(next)
            pos = next
            continue

saved_time_count = defaultdict(int)
for pos in path:
    for dir in DIRS:
        if evaluate_shortcut(pos,dir,path,grid):
            after = tuple_add(pos,tuple_mult(dir,2))
            saved_time = path.index(after) - path.index(pos) - 2
            saved_time_count[saved_time] += 1

print(sum(v for k,v in saved_time_count.items() if k >= 100))