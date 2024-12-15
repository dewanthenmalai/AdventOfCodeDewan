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

def get_robot(grid):
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == '@':
                return np.array([x,y])
    return None

def move_elements(grid, to_move, dir):
    for pos in to_move[::-1]:
        grid_set(grid,pos+dir,grid_get(grid,pos))
        grid_set(grid,pos,'.')

def get_GPS_score(grid):
    score = 0
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == 'O':
                score += 100*y + x
    return score

with open('Input.txt','r') as file:
    input = file.read()

raw_grid, raw_instructions = input.split('\n\n')
grid = [[c for c in row] for row in raw_grid.split('\n')]
instructions = ''.join([row for row in raw_instructions.split('\n')])

for move in instructions:
    dir = DIRS[move]
    robot_pos = get_robot(grid)
    if robot_pos is None:
        print('Could not find robot')
        exit(1)
    to_move = [robot_pos]
    pos = robot_pos
    while True:
        pos = pos+dir
        match grid_get(grid,pos):
            case 'O':
                to_move.append(pos)
            case '#':
                break
            case '.':
                move_elements(grid,to_move,dir)
                break
            case _:
                print(f'Invalid symbol "{grid_get(grid,pos)}"')
                exit(1)

#print('\n'.join([''.join(row) for row in grid]))
print(f'Score: {get_GPS_score(grid)}')