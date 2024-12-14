import numpy as np
import re
from tqdm import tqdm

x_max = 101
y_max = 103

class Robot:
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos = np.array([int(pos_x), int(pos_y)])
        self.vel = np.array([int(vel_x), int(vel_y)])
    
    def advance(self):
        self.pos += self.vel
        self.pos[0] %= x_max
        self.pos[1] %= y_max
    
    def place(self, grid):
        grid[self.pos[1]][self.pos[0]] += 1

def get_extended_position(pos, x_max, y_max):
    x_max = len(grid[0])
    y_max = len(grid)
    return (pos[0]%x_max,pos[1]%y_max)



with open('Input.txt', 'r') as file:
    input = file.read()

pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
matches = re.finditer(pattern, input)
robots = [Robot(*match.groups()) for match in matches]

grid = [[0 for i in range(x_max)] for j in range(y_max)]

seconds = 0
while True:
    seconds += 1
    grid = [[0 for i in range(x_max)] for j in range(y_max)]
    for r in robots:
        r.advance()
        r.place(grid)
    
    if all(i < 2 for row in grid for i in row):
        break

#compare grid visualizations for testing
print('\n'.join([''.join([str(i) for i in row]) for row in grid]))
print(seconds)