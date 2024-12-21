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
    return '_'

def manhattan_circle(center, radius, grid):
    circle = []
    for x in range(center[0]-radius,center[0]+radius+1):
        for y in range(center[1]-radius,center[1]+radius+1):
            if (abs(center[0]-x) + abs(center[1]-y)) == radius:
                if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                    circle.append((x,y))
    return circle

def get_terminus(grid, val):
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == val:
                return (x,y)
    return None

def evaluate_shortcuts(pos, path, grid):
    saved_times = defaultdict(int)
    for i in range(2,21):
        for c in manhattan_circle(pos,i,grid):
            if grid_get(grid, c) in 'SE.' and c in path:
                if path.index(pos) < path.index(c):
                    saved_time = path.index(c) - path.index(pos) - i
                    saved_times[saved_time] += 1
    return saved_times

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
    saved_times = evaluate_shortcuts(pos,path,grid)
    for k,v in saved_times.items():
        saved_time_count[k] += v
 
# for k,v in sorted(saved_time_count.items()):
    # print(f'There are {v} cheats that save {k} picoseconds.')
print(sum(v for k,v in saved_time_count.items() if k >= 100))