import numpy as np
import re
from tqdm import tqdm

def get_extended_position(pos, x_max, y_max):
    x_max = len(grid[0])
    y_max = len(grid)
    return (pos[0]%x_max,pos[1]%y_max)

with open('Input.txt', 'r') as file:
    input = file.read()

pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
matches = re.finditer(pattern, input)
robots = [match.groups() for match in matches]
x_max = 101
y_max = 103

grid = [[0 for i in range(x_max)] for j in range(y_max)]

for robot in tqdm(robots):
    p = np.array([int(robot[0]),int(robot[1])])
    v = np.array([int(robot[2]),int(robot[3])])
    pos = p + (100*v)
    tele_pos = get_extended_position(pos,x_max,y_max)
    grid[tele_pos[1]][tele_pos[0]] += 1

#compare grid visualizations for testing
#print('\n'.join([''.join([str(i) for i in row]) for row in grid]))
quad_1 = sum(i for row in grid[:y_max//2] for i in row[:x_max//2])
quad_2 = sum(i for row in grid[:y_max//2] for i in row[x_max//2+1:])
quad_3 = sum(i for row in grid[y_max//2+1:] for i in row[:x_max//2])
quad_4 = sum(i for row in grid[y_max//2+1:] for i in row[x_max//2+1:])
#print(quad_1,quad_2,quad_3,quad_4)
print(quad_1*quad_2*quad_3*quad_4)