import numpy as np

DIRS = {
    '>': np.array([1,0]),
    '<': np.array([-1,0]),
    'v': np.array([0,1]),
    '^': np.array([0,-1])
    }

def grid_get(grid, pos):
    return grid[pos[1]][pos[0]]

def grid_set(grid, pos, val):
    grid[pos[1]][pos[0]] = val

def extend_grid(grid):
    extended_grid = [[] for _ in  range(len(grid))]
    for y,row in enumerate(grid):
        for c in row:
            match c:
                case '#':
                    extended_grid[y].extend(['#','#'])
                case 'O':
                    extended_grid[y].extend(['[',']'])
                case '.':
                    extended_grid[y].extend(['.','.'])
                case '@':
                    extended_grid[y].extend(['@','.'])
    return extended_grid

def get_robot(grid):
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == '@':
                return np.array([x,y])
    return None

def move_elements(grid, to_move, dir):
    moved = set()
    for pos in to_move[::-1]:
        if tuple(pos) in moved:
            continue
        grid_set(grid,pos+dir,grid_get(grid,pos))
        grid_set(grid,pos,'.')
        moved.add(tuple(pos))

def can_push_vertical(grid, pos, dir):
    match grid_get(grid,pos+dir):
        case '.':
            return True
        case '#':
            return False
        case '[':
            return can_push_vertical(grid,pos+dir,dir) and can_push_vertical(grid,pos+dir+DIRS['>'],dir)
        case ']':
            return can_push_vertical(grid,pos+dir,dir) and can_push_vertical(grid,pos+dir+DIRS['<'],dir)

def push_vertical(grid, pos, dir):
    match grid_get(grid,pos+dir):
        case '.':
            grid_set(grid,pos+dir,grid_get(grid,pos))
            grid_set(grid,pos,'.')
        case ']':
            push_vertical(grid,pos+dir,dir)
            push_vertical(grid,pos+dir+DIRS['<'],dir)
            grid_set(grid,pos+dir,grid_get(grid,pos))
            grid_set(grid,pos,'.')
        case '[':
            push_vertical(grid,pos+dir,dir)
            push_vertical(grid,pos+dir+DIRS['>'],dir)
            grid_set(grid,pos+dir,grid_get(grid,pos))
            grid_set(grid,pos,'.')

def get_GPS_score(grid):
    score = 0
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == '[':
                score += 100*y + x
    return score

with open('Input.txt','r') as file:
    input = file.read()

raw_grid, raw_instructions = input.split('\n\n')
narrow_grid = [[c for c in row] for row in raw_grid.split('\n')]
instructions = ''.join([row for row in raw_instructions.split('\n')])
grid = extend_grid(narrow_grid)

for move in instructions:
    dir = DIRS[move]
    robot_pos = get_robot(grid)
    if robot_pos is None:
        print('Could not find robot')
        exit(1)
    pos = robot_pos
    if move in '<>':
        to_move = [robot_pos]
        while True:
            pos = pos+dir
            match grid_get(grid,pos):
                case '[' | ']':
                    to_move.append(pos)
                case '#':
                    break
                case '.':
                    move_elements(grid,to_move,dir)
                    break
                case _:
                    print(f'Invalid symbol "{grid_get(grid,pos)}"')
                    exit(1)
    elif can_push_vertical(grid,pos,dir):
            push_vertical(grid,pos,dir)

#print('\n'.join([''.join(row) for row in grid]))
print(f'Score: {get_GPS_score(grid)}')