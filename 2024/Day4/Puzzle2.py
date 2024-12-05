NONE = 0
RIGHT = 1
LEFT = -1
UP = -1
DOWN = 1

def count_direction(grid, row, col, dirRow, dirCol):
    keyword = 'MAS'
    for c in keyword:
        if row < 0 or row >= rows:
            return 0
        if col < 0 or col >= cols:
            return 0
        if grid[col][row] != c:
            return 0
        row += dirRow
        col += dirCol
    return 1

def count_cross(grid, row, col):
    count = (count_direction(grid, row+LEFT, col+UP, RIGHT, DOWN) +
             count_direction(grid, row+LEFT, col+DOWN, RIGHT, UP) +
             count_direction(grid, row+RIGHT, col+UP, LEFT, DOWN) +
             count_direction(grid, row+RIGHT, col+DOWN, LEFT, UP))
    return 1 if count == 2 else 0

with open('Input.txt', 'r') as file:
    lines = file.readlines()

grid = [[c for c in line.rstrip()] for line in lines]
count = 0
cols = len(grid)
rows = len(grid[0])

for i in range(1, rows-1):
    for j in range(1, cols-1):
        count += count_cross(grid, i, j)

print(count)